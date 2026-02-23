from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

citiest=['sitka','death_valley']
paths=['Data_16/weather_data/death_valley_2021_simple.csv','Data_16/weather_data/sitka_weather_2021_simple.csv']

plt.style.use('classic')
fig, ax=plt.subplots()
for path_s in paths:
    path=Path(path_s)
    lines=path.read_text().splitlines()
    reader=csv.reader(lines)
    header_row=next(reader)
    print(path)
    for index,column_header in enumerate(header_row):
        if column_header=='DATE':
            Date_index=index
            print(Date_index)
        if column_header=='TMAX':
            TMAX_index=index
        if column_header=='TMIN':
            TMIN_index=index
    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[Date_index], '%Y-%m-%d')
        try:
            high=float(row[TMAX_index])
            low=float(row[TMIN_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    ax.plot(dates,highs,color='red',alpha=0.5)
    ax.plot(dates,lows,color='blue',alpha=0.5)
    ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    
text_title="Daily highs and low temperatures: "
for city in citiest:
    text_title=text_title + city+ ','
text_title=text_title + ' 2021'
 #Задание заголовка диаграммы и меток осей.
ax.set_title(text_title, fontsize=15)
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
