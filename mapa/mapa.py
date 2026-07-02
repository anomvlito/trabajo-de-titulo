import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from matplotlib.patches import Patch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.colors import ListedColormap, BoundaryNorm
from geopy.distance import geodesic
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerBase

## VARIABLES
evaluation_ratio = 2 #km

path_info_gse = "Datasets/grupos_gse_por_manzana_censo_2012.geojson"
path_comunas = "Datasets/13.geojson"
path_stores = "Datasets/locales.geojson"

path_icon_stores = "pins/deep-blue.png"
path_icon_upcoming_stores = "pins/bright-blue.png"
path_icon_competence = "pins/pink.png"
path_icon_stores_to_evaluate = "pins/cian.png"

gse_column = "GSE_final"
gse_index_column = "GSE_index"
column_quintil = "quintil"

# Colores
hex_stores = '#1E3A8A'
hex_upcoming_stores = '#3B82F6'
hex_stores_to_evaluate = '#00D1C1'
hex_primary_competence = '#4B236A'
hex_secondary_competence = '#7D3C98'
hex_supermarkets = '#872657'
hex_lines = '#383838'
hex_gse_colors = ['#C9463B', '#D67D32', '#E3B329', '#9EA843', '#4A814D']  # E -> ABC1
hex_gse_unknown = '#E8E8E8' 

# Cargar archivos
info_gse_gdf = gpd.read_file(path_info_gse)
comunas_gdf = gpd.read_file(path_comunas)
tiendas_gdf = gpd.read_file(path_stores)

# Pin
local_pin = plt.imread(path_icon_stores)
prox_local_pin = plt.imread(path_icon_upcoming_stores)
competencia_pin = plt.imread(path_icon_competence)
stores_to_evaluate_pin = plt.imread(path_icon_stores_to_evaluate)

# Filtrar comunas
comunas_gdf = comunas_gdf[~comunas_gdf['Comuna'].isin([
    'Buin', 'Calera de Tango', 'Paine', 'Pirque', 'San José de Maipo',
    'Talagante', 'El Monte', 'Melipilla', 'Curacaví', 'María Pinto',
    'San Pedro', 'Alhué', 'Lampa', 'Tiltil', 'Colina',
    'Isla de Maipo', 'Peñaflor'
])]

# Reemplazar espacios por 'Desconocido'
info_gse_gdf[gse_column] = info_gse_gdf[gse_column].replace(' ', 'Desconocido')

# Mapear grupos socioeconómicos a índices
gse_map = {'ABC1': 5, 'C2': 4, 'C3': 3, 'D': 2, 'E': 1}
info_gse_gdf[gse_index_column] = info_gse_gdf[gse_column].map(gse_map)

# Crear colormap
labels = ['E', 'D', 'C3', 'C2', 'ABC1']  # De menor a mayor GSE
bounds = [1, 2, 3, 4, 5, 6]  # Uno más que el máximo índice

cmap = ListedColormap(hex_gse_colors)
norm = BoundaryNorm(bounds, cmap.N)

# Separar GSE conocidos de los desconocidos
gdf_conocido = info_gse_gdf[info_gse_gdf[gse_column] != 'Desconocido']
gdf_desconocido = info_gse_gdf[info_gse_gdf[gse_column] == 'Desconocido']

# Graficar conocidos con colormap
fig, ax = plt.subplots(figsize=(12, 7))
gdf_conocido.plot(
    column=gse_index_column,
    cmap=cmap,
    norm=norm,
    edgecolor=hex_lines,
    linewidth=0.07,
    ax=ax
)

# Graficar desconocidos en gris claro
gdf_desconocido.plot(
    color=hex_gse_unknown,
    edgecolor=hex_lines,
    linewidth=0.07,
    ax=ax
)

# Guardar límites del primer gráfico
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Dibujar comunas sobre el mapa
comunas_gdf.plot(
    ax=ax,
    color='none',
    edgecolor=hex_lines,
    linewidth=0.7,
)

# Graficar locales
gdf_stores = tiendas_gdf[tiendas_gdf['type'] == 'local-actual']
gdf_upcoming_stores = tiendas_gdf[tiendas_gdf['type'] == 'local-prox']
gdf_primary_competence = tiendas_gdf[tiendas_gdf['type'] == 'competencia']
gdf_secondary_competence = tiendas_gdf[tiendas_gdf['type'] == 'competencia-secundaria']
gdf_supermarket = tiendas_gdf[tiendas_gdf['type'] == 'supermercados']
gdf_stores_to_evaluate = tiendas_gdf[tiendas_gdf['type'] == 'local-propuesto']

for idx, row in gdf_secondary_competence.iterrows():
    x, y = row.geometry.x, row.geometry.y
    ax.plot(x, y, 'o', color=hex_secondary_competence, markersize=4)  # Puedes cambiar color y tamaño

for idx, row in gdf_supermarket.iterrows():
    x, y = row.geometry.x, row.geometry.y
    ax.plot(x, y, 'o', color=hex_supermarkets, markersize=4)  # Puedes cambiar color y tamaño

for idx, row in gdf_primary_competence.iterrows():
    x, y = row.geometry.x, row.geometry.y
    ax.plot(x, y, 'o', color=hex_primary_competence, markersize=4)  # Puedes cambiar color y tamaño

for idx, row in gdf_stores.iterrows():
    x, y = row.geometry.x, row.geometry.y
    imagebox = OffsetImage(local_pin, zoom=0.3)  # Ajusta el zoom según el tamaño del ícono
    ab = AnnotationBbox(imagebox, (x, y), frameon=False)
    ax.add_artist(ab)

for idx, row in gdf_upcoming_stores.iterrows():
    x, y = row.geometry.x, row.geometry.y
    imagebox = OffsetImage(prox_local_pin, zoom=0.3)  # Ajusta el zoom según el tamaño del ícono
    ab = AnnotationBbox(imagebox, (x, y), frameon=False)
    ax.add_artist(ab)

for idx, row in gdf_stores_to_evaluate.iterrows():
    x, y = row.geometry.x, row.geometry.y
    imagebox = OffsetImage(stores_to_evaluate_pin, zoom=0.3)  # Ajusta el zoom según el tamaño del ícono
    ab = AnnotationBbox(imagebox, (x, y), frameon=False)
    ax.add_artist(ab)

# Crear un círculo de 1 km alrededor del centro
    center = (row.geometry.y, row.geometry.x)
    circle_points = []
    for angle in range(0, 360):
        point = geodesic(kilometers=evaluation_ratio).destination(center, angle)
        circle_points.append((point.longitude, point.latitude))
    lons, lats = zip(*circle_points)
    ax.plot(lons, lats,color=hex_stores_to_evaluate)
    ax.fill(lons, lats, facecolor='skyblue', edgecolor='blue', alpha=0.3, label='Área 1 km')


# Crear leyenda personalizada
gse_legend_labels = {
    'ABC1': 5,
    'C2': 4,
    'C3': 3,
    'D': 2,
    'E': 1,
    'Desconocido': None
}

gse_legend_patches = [
    mpatches.Patch(color=cmap(norm(val)), label=gse)
    for gse, val in gse_legend_labels.items() if val is not None
]
# Agregar color gris para Desconocido
gse_legend_patches.append(mpatches.Patch(color='lightgrey', label='Desconocido'))

## LEYENDAS

# Leyenda de GSE
gse_legend = ax.legend(
    handles=gse_legend_patches,
    title='Grupo Socioeconómico',
    loc='center left',
    bbox_to_anchor=(1.02, 0.7),
    frameon=True
)
ax.add_artist(gse_legend)

# Leyenda de Locales
stores_legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Locales', markerfacecolor=hex_stores, markersize=12),
    Line2D([0], [0], marker='o', color='w', label='Próximos locales', markerfacecolor=hex_upcoming_stores, markersize=12),
    Line2D([0], [0], marker='o', color='w', label='Locales a evaluar', markerfacecolor=hex_stores_to_evaluate, markersize=12),
]

stores_legend = ax.legend(
    handles=stores_legend_elements,
    title='Locales',
    loc='center left',
    bbox_to_anchor=(1.02, 0.5),  # Ajusta este valor si necesitas moverla más arriba/abajo
    frameon=True
)

ax.add_artist(stores_legend)

# Leyenda de la competencia
competence_legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Competencia Directa', markerfacecolor=hex_primary_competence, markersize=12),
    Line2D([0], [0], marker='o', color='w', label='Competencia Secundaria', markerfacecolor=hex_secondary_competence, markersize=12),
    Line2D([0], [0], marker='o', color='w', label='Supermercados', markerfacecolor=hex_supermarkets, markersize=12),
]

competence_legend = ax.legend(
    handles=competence_legend_elements,
    title='Competencia',
    loc='center left',
    bbox_to_anchor=(1.02, 0.35),  # Ajusta este valor si necesitas moverla más arriba/abajo
    frameon=True
)

ax.add_artist(competence_legend)


# Títulos y ajustes
fig.patch.set_facecolor('white')
plt.title("Mapa de Cuadras de Santiago por Grupo Socioeconómico")
plt.axis('off')
plt.tight_layout(pad=0)
plt.subplots_adjust(top=0.95)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.savefig("mi_mapa.png", dpi=300, bbox_inches='tight', pad_inches=0, bbox_extra_artists=[gse_legend, stores_legend, competence_legend])
plt.show()


