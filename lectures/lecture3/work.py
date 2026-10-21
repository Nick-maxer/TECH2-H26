import matplotlib.pyplot as plt


x_values = range(-50, 50)
y_values = [x**2 for x in x_values]

graph = plt.plot(x_values, y_values)

plt.show() 