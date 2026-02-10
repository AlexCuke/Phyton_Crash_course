import matplotlib.pyplot as plt
#print(plt.style.available)
#input_values = [1,2,3,4,5]
#squares=[1,4,9,16,25]
x_values=range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8-colorblind')
fig, ax =plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues, s=10 )

#Задание заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

 #Задание заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#Задание размера шрифта делений на осях.
ax.tick_params(axis='both', labelsize=10)

#Задание диапазлга ждя каждой оси
ax.axis([0,1100,0,1_100_000])
ax.ticklabel_format(style='plain')
plt.savefig('squares_plot.png',bbox_inches='tight')


