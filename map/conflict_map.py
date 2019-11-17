import csv
import pandas as pd
import folium

df = pd.read_csv("Conflict Data for Greece.csv", header=0)
if 0 in df.index:
    df.drop([0], inplace=True)
df.info()

print(df.head())
print(df['event_type'].unique())


df["latitude"] = df["latitude"].astype(str).astype(float)
df["longitude"] = df["longitude"].astype(str).astype(float)
latitude_mean = df["latitude"].astype(float).mean()
longitude_mean = df["longitude"].astype(float).mean()
map = folium.Map([latitude_mean, longitude_mean])

for i in range(len(df)):
    color = 'red'

    if df.iloc[i]['event_type'] == 'Protests':
        color = 'blue'
    elif df.iloc[i]['event_type'] == 'Riots':
        color = 'yellow'
    elif df.iloc[i]['event_type'] == 'Battles':
        color = 'green'


    folium.CircleMarker(
        [df.iloc[i]["latitude"], df.iloc[i]["longitude"]],
        radius=5 + int(df.iloc[i]["fatalities"]),
        fill=True,
        color=color
    ).add_to(map)


map.save(outfile="greece.html")
