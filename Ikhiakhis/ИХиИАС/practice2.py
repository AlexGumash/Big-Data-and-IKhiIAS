# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

dots = {}

for x in np.linspace(-4, 5, 100):
    dots[x] = 3 * (x**3) - 2 * (x**2) - 7 * x + 9 + np.random.uniform(-10,10)

dots_x = list(dots)
dots_y = list(dots.values())

coefs = np.polyfit(dots_x, dots_y, 3)
print(coefs)


plt.scatter(
    dots_x,
    dots_y,
    c='red'
)

plt.plot(
    dots_x,
    np.polyval(coefs, dots_x),
    'blue'
)
plt.grid(False)
plt.show()
