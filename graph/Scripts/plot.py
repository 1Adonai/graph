import matplotlib.pyplot as plt
import numpy as np


path = '/home/rumin/Documents/Code/Web/graph/War/numbers.txt'
file = open(path,'r')
num = file.read().splitlines()
s1 = int(num[0])
r1 = int(num[1])
b1 = float(num[2])
file.close()


def lorenz(xyz, *, s=s1, r=r1, b=b1):
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])


dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (0., 1., 1.05)  # Set initial values

path = '/home/rumin/Documents/Code/Web/graph/War/numbers.txt'
file = open(path,'r')
num = file.read().splitlines()
s = int(num[0])
r = int(num[1])
b = float(num[2])
file.close()


for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

# Plot
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

# Сохранение графика с указанием пути
plt.savefig('/home/rumin/Documents/Code/Web/graph/static/main/img/plot.png')

