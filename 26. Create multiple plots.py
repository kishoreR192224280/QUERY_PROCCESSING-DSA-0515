import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Creating multiple subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plotting on first axis
ax1.plot(x, y1, label='Line 1', color='blue')
ax1.set_title('First Plot')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')

# Plotting on second axis
ax2.plot(x, y2, label='Line 2', color='red')
ax2.set_title('Second Plot')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')

# Display the plot
plt.tight_layout()
plt.show()
