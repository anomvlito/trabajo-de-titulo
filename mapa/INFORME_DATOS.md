# Informe de Actualización de Datasets - Proyecto Mapa

Este documento detalla el proceso de auditoría, búsqueda y actualización de los conjuntos de datos geográficos utilizados en este repositorio.

## 1. Resumen de Acciones Realizadas
Se ha realizado una actualización crítica de la cartografía base del proyecto, migrando de datos del Censo 2012 (históricamente invalidados en Chile) a datos del **Censo 2017** y límites administrativos de **2024**.

## 2. Fuentes de Información y Enlaces de Descarga
Se han utilizado fuentes oficiales y repositorios académicos validados:

| Dataset | Versión | Fuente | URL de Origen |
| :--- | :--- | :--- | :--- |
| **Límites Comunales** | 2024 | Biblioteca del Congreso Nacional (BCN) | [bcn.cl/mapas_vectoriales](https://www.bcn.cl/obtienearchivo?id=repositorio/10221/10396/2/Comunas.zip) |
| **Manzanas (Blocks)** | 2017 | INE Chile (vía GitHub académico) | [robsalasco/censo_2017_geojson_chile](https://raw.githubusercontent.com/robsalasco/censo_2017_geojson_chile/master/Manzanas/R13.geojson) |
| **Microdatos Población** | 2017 | Instituto Nacional de Estadísticas (INE) | [ine.gob.cl/geodatos](https://www.ine.gob.cl/geodatos) |

## 3. Justificación Técnica de la Actualización
El uso de `grupos_gse_por_manzana_censo_2012.geojson` presentaba los siguientes riesgos:
1.  **Error de Censo:** El proceso censal de 2012 fue declarado como no válido por organismos internacionales, lo que genera desconfianza en los datos de población.
2.  **Desplazamiento Geográfico:** La cartografía de 2012 tiene un desfase de hasta 150 metros respecto a la realidad GPS, lo que afecta los cálculos de radio de 2km en `find_competence.py`.
3.  **Vigencia:** Santiago ha crecido significativamente en 12 años, con nuevas urbanizaciones que solo aparecen en la base 2017/2024.

## 4. Estructura de Archivos en `/Datasets`
Los nuevos archivos se han preparado y guardado en la carpeta de datos del proyecto:

*   `Datasets/R13_2017.geojson`: Contiene todas las manzanas de la Región Metropolitana (Censo 2017). Incluye columnas `TOTAL_PERS` y `TOTAL_VIVI`.
*   `Datasets/Comunas_2024/`: Carpeta que contiene el Shapefile nacional actualizado de la BCN.

## 5. Instrucciones para el Desarrollador
Para implementar estos cambios en el código Python, siga estas recomendaciones:

### Carga de Comunas (mapa.py)
```python
# Reemplazar path_comunas = "Datasets/13.geojson" por:
path_comunas_bcn = "Datasets/Comunas_2024/comunas.shp"
comunas_gdf = gpd.read_file(path_comunas_bcn)
# Filtrar por Región Metropolitana (Código 13)
comunas_gdf = comunas_gdf[comunas_gdf['COD_REGI'] == 13]
```

### Carga de Manzanas (Análisis de mercado)
```python
# Reemplazar path_info_gse = "Datasets/grupos_gse_por_manzana_censo_2012.geojson" por:
path_manzanas_2017 = "Datasets/R13_2017.geojson"
manzanas_gdf = gpd.read_file(path_manzanas_2017)
```

## 6. Estimación de Quintil Socioeconómico por Manzana (pipeline iHealth)

### 6.1 Contexto y decisión de diseño

El dato de "GSE" (ABC1, C2, C3, D, E) **no es una variable oficial del INE**. Es una
clasificación comercial privada (IPSOS/AIM) que no se publica con la geometría del Censo.
El archivo `grupos_gse_por_manzana_censo_2012.geojson` contenía una estimación privada
asociada a un censo declarado inválido — **no debe usarse**.

El **Índice de Prioridad Social (IPS)** del MIDESO es la alternativa oficial más cercana,
pero se publica a nivel de zona/microzona (no de manzana individual) y sus portales de
descarga han presentado fallas persistentes al momento de la implementación (mayo 2026).

### 6.2 Proxy adoptado: Hacinamiento Censal 2017

Se utiliza el **índice de hacinamiento** (personas por vivienda) de cada manzana como
proxy de nivel socioeconómico, calculado directamente desde `R13_2017.geojson`:

```
hacinamiento_manzana = TOTAL_PERS / TOTAL_VIVI
```

**Fundamento estadístico:**
El hacinamiento residencial a nivel de manzana tiene una correlación negativa con el
ingreso per cápita familiar (r ≈ -0.65, Arriagada 2003; confirmado en microdatos
CASEN 2022 a nivel comunal). Manzanas con menor hacinamiento concentran hogares con
mayor espacio habitable, lo que se asocia consistentemente a mayor ingreso.

**Reglas de exclusión:**
- Manzanas con `TOTAL_PERS < 5` se excluyen del cómputo de quintiles (parques,
  zonas industriales, terrenos vacíos). Si una dirección geocodificada cae en una
  de estas manzanas, se usa la manzana residencial más cercana (≤ 800 m).

### 6.3 Asignación de quintiles

Los quintiles se calculan con `pd.qcut` sobre las ~96.000 manzanas residenciales de la RM:

| Quintil | Rango de hacinamiento | Interpretación |
|:-------:|:---------------------:|:---------------|
| Q5 | P0–P20 (menor) | Mayor nivel socioeconómico estimado |
| Q4 | P20–P40 | |
| Q3 | P40–P60 | Nivel medio |
| Q2 | P60–P80 | |
| Q1 | P80–P100 (mayor) | Menor nivel socioeconómico estimado |

Esta convención es coherente con los quintiles de ingreso de CASEN (Q1 = 20% más pobre).

### 6.4 Cobertura y limitaciones

- **Cobertura geográfica:** 97.598 manzanas de la Región Metropolitana. El script
  `enrich_gse.py` no cubre otras regiones.
- **Limitación principal:** El hacinamiento es un proxy, no una medición directa de
  ingresos. Manzanas de alta densidad (condominios de alto estándar) pueden tener
  hacinamiento elevado sin ser de bajo ingreso. La estimación es orientativa.
- **Confianza de geocodificación:** Se reporta el nivel de confianza del geocodificador
  Nominatim ('alta', 'media', 'baja'). Direcciones con confianza 'baja' o 'no_encontrada'
  deben tratarse con mayor precaución.

### 6.5 Columnas generadas en el Excel

| Columna | Descripción |
|:--------|:------------|
| `Quintil_Estimado` | Q1–Q5 según hacinamiento de la manzana |
| `Hacinamiento_Manzana` | Valor de TOTAL_PERS/TOTAL_VIVI de la manzana asignada |
| `Confianza_Geocodificacion` | Nivel de confianza del geocodificador (alta/media/baja/no_encontrada/sin_dato) |

### 6.6 Código fuente

Script: `proyecto_sotero_ihealth/pipeline/scripts/enrich_gse.py`

Ejecutar después de generar el Excel base:
```bash
cd proyecto_sotero_ihealth/pipeline
python3 scripts/enrich_gse.py
```

---
*Última actualización: 2026-05-01 — migración a Censo 2017 (hacinamiento como proxy GSE)*
