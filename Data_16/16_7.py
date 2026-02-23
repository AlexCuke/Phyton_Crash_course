from pathlib import Path
import json
import plotly.express as px

#Cчитывает данные в строковме формате
path=Path('eq_data/1_month.geojson')
with open(path, encoding='utf-8') as f:
    all_eq_data = json.load(f)


#создвает удобную для чтения версию файла данных
path=Path('eq_data/1_1_month.geojson')
readable_content=json.dumps(all_eq_data, indent=4)
path.write_text(readable_content)

#обработка всех землятресений в наборе данных
title=all_eq_data['metadata']['title']  

all_eq_dicts=all_eq_data['features']
print(len(all_eq_dicts))

mags,lons,lats,eq_titles=[],[],[],[]
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])


title=title
fig=px.scatter_geo(lat=lats,
lon=lons,
color=mags,
size=mags,
title=title,
color_continuous_scale='Viridis',projection='natural earth',hover_name=eq_titles)
fig.show()