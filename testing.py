import matplotlib.pyplot as plt
import numpy as np
import math



def main():
    vectorDensity = 20 #How many vectors graphed
    xMin = -10
    xMax = 10
    yMin = -10
    yMax = 10
    x, y = np.meshgrid(np.linspace(xMin, xMax, vectorDensity),  np.linspace(yMin, yMax, vectorDensity)) 

    u = -((x**2)+(y**2))
    v = x*y
    plt.grid()
    plt.tight_layout()
    plt.quiver(x,y,u,v, pivot='mid')
    
    plt.show()



if __name__ == "__main__":
    main()