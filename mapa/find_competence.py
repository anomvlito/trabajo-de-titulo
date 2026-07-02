import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

path_stores = "Datasets/locales.geojson"
ratio_evaluation = 2  # km

# Carga el GeoJSON
gdf_stores = gpd.read_file(path_stores)

gdf_competence = gdf_stores[~gdf_stores['type'].isin(['local-propuesto'])]
gdf_stores_to_evaluate = gdf_stores[gdf_stores['type'].isin(['local-propuesto', 'local-actual'])]

# Asume que el GeoJSON usa coordenadas en WGS84
gdf_competence = gdf_competence.set_crs(epsg=4326)

# Convierte a una proyección métrica para calcular distancias en metros
gdf_competence = gdf_competence.to_crs(epsg=32719)  # UTM zona 19S, adecuada para Chile central

distances = {}
for stores_to_evaluate in gdf_stores_to_evaluate.iterrows():
    gdf_competence_2 = gdf_competence.copy()
    # Crea un punto de referencia a partir de las coordenadas
    punto_referencia = Point(stores_to_evaluate[1]['geometry'].x, stores_to_evaluate[1]['geometry'].y)
    punto_referencia_utm = gpd.GeoSeries([punto_referencia], crs="EPSG:4326").to_crs(epsg=32719).iloc[0]

    # Filtra los puntos que están a menos de 2 km (2000 metros)
    gdf_competence_2["distance"] = gdf_competence_2.geometry.distance(punto_referencia_utm)
    gdf_filtrado = gdf_competence_2[gdf_competence_2["distance"] <= ratio_evaluation * 1000]

    df = pd.DataFrame(gdf_filtrado)
    df['distance'] = df['distance'] / 1000  # Convertir a kilómetros
    df = df.drop(columns=['geometry'])
    df = df.sort_values(by='distance')
    distances[stores_to_evaluate[1]['name']] = df

with pd.ExcelWriter('resultados_locales_propuestos.xlsx', engine='openpyxl') as writer:
    for store_to_evaluate, df in distances.items():
        df.to_excel(writer, sheet_name=store_to_evaluate, index=False)
