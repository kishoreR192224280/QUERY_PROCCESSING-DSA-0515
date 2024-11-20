import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Define colors for each bar
colors = ['blue', 'green', 'red', 'yellow', 'purple', 'orange']

# Creating a bar chart with different colors
plt.bar(languages, popularity, color=colors)

# Adding title and labels
plt.title('Popularity of Programming Languages (Different Colors)')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')

# Display the plot
plt.show()
