from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

#path=Path('Data_16/weather_data/sitka_weather_07-2021_simple.csv')
path_DV=Path('Data_16/weather_data/death_valley_2021_simple.csv')
lines_dv=path_DV.read_text().splitlines()
reader_DV=csv.reader(lines_dv)
header_row_DV=next(reader_DV)
path_SW=Path('Data_16/weather_data/sitka_weather_2021_simple.csv')
lines_SW=path_SW.read_text().splitlines()
reader_SW=csv.reader(lines_SW)
header_row_SW=next(reader_SW)
print('DV')
for index,column_header in enumerate(header_row_DV):
    print(index,column_header)
print('SW')
for index,column_header in enumerate(header_row_SW):
    print(index,column_header)
    
dates_DV,highs_DV,lows_DV=[],[],[]
for row in reader_DV:
    current_date=datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high=float(row[3])
        low=float(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates_DV.append(current_date)
        highs_DV.append(high)
        lows_DV.append(low)
dates_SW,highs_SW,lows_SW=[],[],[]
for row in reader_SW:
    current_date=datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high=float(row[4])
        low=float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates_SW.append(current_date)
        highs_SW.append(high)
        lows_SW.append(low)


plt.style.use('classic')
fig, ax=plt.subplots()
ax.plot(dates_SW,highs_SW,color='red',alpha=0.5)
ax.plot(dates_SW,lows_SW,color='blue',alpha=0.5)
ax.fill_between(dates_SW,highs_SW,lows_SW,facecolor='blue',alpha=0.1)

ax.plot(dates_DV,highs_DV,color='red',alpha=0.7)
ax.plot(dates_DV,lows_DV,color='yellow',alpha=0.7)
ax.fill_between(dates_DV,highs_DV,lows_DV,facecolor='yellow',alpha=0.1)

 #Задание заголовка диаграммы и меток осей.
#ax.set_title("Daily temperatures, July 2021", fontsize=24)
ax.set_title("Daily hihgs and low temperatures, Sitka, Death valley 2021", fontsize=15)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
#Задание размера шрифта делений на осях.
ax.tick_params (labelsize=14)


plt.show()





'''dates,highs,lows=[],[],[]
for row in reader:
    current_date=datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high=int(row[3])
        low=int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)






'''
