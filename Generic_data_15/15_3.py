import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    #Создание случайного блуждания
    rw=RandomWalk(10_000)
    rw.fill_walk()

    #Нанесение точек на диаграмму
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(15,9),dpi=128)
    point_numbers=range(rw.num_points)
    #ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    ax.plot(rw.x_values,rw.y_values,linewidth=1)
    ax.set_aspect('equal')
    #Выделение первой и последней точки цветом
    ax.scatter(0,0,c='green',edgecolors='none',s=10)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)
    ax.set_aspect('equal')
    #Выделение первой и последней точки цветом
    ax.scatter(0,0,c='green',edgecolors='none',s=10)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)
    ax.set_aspect('equal')
    #цдвление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running=input("Make another walk? (y/n): ")
    if keep_running=='n':
        break