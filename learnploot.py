import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_aspect('equal')  # Set the aspect ratio to be equal

xmin, xmax = -0.2, 1.4
X = np.arange(xmin, xmax, 0.1)
ax.scatter(0, 0, color="r", label="Class 1")
ax.scatter(0, 1, color="r", label="Class 1")
ax.scatter(1, 0, color="r", label="Class 1")
ax.scatter(1, 1, color="g", label="Class 2")
ax.set_xlim([xmin, xmax])
ax.set_ylim([-0.1, 1.1])
m = -1
ax.plot(X, m * X + 1.2, label="Decision Boundary")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

plt.show()
