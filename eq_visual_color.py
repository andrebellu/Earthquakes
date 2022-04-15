import json
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout


file = 'Python Crash Course\DATA VISUALIZATION\Downloading Data\Earthquakes\data\eq_data_30_day_m1.json'

with open(file) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hovers = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hovers.append(title)

data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'colorscale' : 'viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'},
    },
    'text' : hovers,
}]
my_layout = Layout(title='Global Earthquakes',)

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='global_hearthquakes.html')


    
