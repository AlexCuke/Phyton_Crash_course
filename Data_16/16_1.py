from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

#path=Path('Data_16/weather_data/sitka_weather_07-2021_simple.csv')
path=Path('Data_16/weather_data/sitka_weather_2021_full.csv')
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header_row=next(reader)

for index,column_header in enumerate(header_row):
    print(index,column_header)
print(header_row)

PRCPS,dates=[],[]
for row in reader:
    current_date=datetime.strptime(row[2], '%Y-%m-%d')
    try:

        PRCP=float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)

        PRCPS.append(PRCP)

fig, ax=plt.subplots()

ax.plot(dates,PRCPS,color='blue',alpha=0.5)

ax.set_title("Daily water ,  2021\nSitka", fontsize=20)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Water (m)", fontsize=14)
#Задание размера шрифта делений на осях.
ax.tick_params (labelsize=14)


plt.show()

'''plt.style.use('classic')
fig, ax=plt.subplots()
ax.plot(dates,highs,color='red',alpha=0.5)
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#Задание заголовка диаграммы и меток осей.
#ax.set_title("Daily temperatures, July 2021", fontsize=24)
ax.set_title("Daily highs and low temperatures,  2021\nDeath valley,CA", fontsize=20)

ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
 #Задание заголовка диаграммы и меток осей.
#ax.set_title("Daily temperatures, July 2021", fontsize=24)
ax.set_title("Daily hihgs and low temperatures,  2021", fontsize=24)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
#Задание размера шрифта делений на осях.
ax.tick_params (labelsize=14)


plt.show()

'''