import matplotlib.pyplot as plt

# Reading data from the file
x, y = [], []
with open('test.txt') as file:
    for line in file:
        xi, yi = map(int, line.split())
        x.append(xi)
        y.append(yi)

# Plotting the data
plt.plot(x, y)

# Adding title and labels
plt.title('Line Plot from File Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
