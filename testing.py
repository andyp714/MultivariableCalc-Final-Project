import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math



def main():

    ballXY = [5,0]
    vectorDensity = 40 #How many vectors graphed
    timeIncrement = 0.1 #time increment between points
    pointsAmount = 1000 #how many calculations



    xMin = -50
    xMax = 50
    yMin = -50
    yMax = 50
    pointX = []
    pointY = []

    for i in range(pointsAmount):
        oldX = ballXY[0]
        oldY = ballXY[1]
        newX = (oldY * timeIncrement) + oldX
        newY = (oldX * -1 * timeIncrement) + oldY
        pointX.append(newX)
        pointY.append(newY)
        ballXY = [newX,newY]
    
    print(pointX)

    x, y = np.meshgrid(np.linspace(xMin, xMax, vectorDensity),  np.linspace(yMin, yMax, vectorDensity)) 

    u = y
    v = -x
    fig = plt.figure()
    plt.grid()
    plt.tight_layout()
    #plt.plot(ballXY[0], ballXY[1], 'ro')
    plt.quiver(x,y,u,v, pivot='mid')
    line, = plt.plot([],[], 'bo')



    def init():
        line.set_data([],[])
        return line,


    def animate(i):
        x = pointX[i]
        y = pointY[i]

        line.set_data([x], [y])
        return line, 

    anim = animation.FuncAnimation(fig, animate, init_func= init, interval = 1, blit=True, frames=pointsAmount, repeat=True)
    plt.show()



if __name__ == "__main__":
    main()