import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Creating a horizontal bar chart
plt.barh(languages, popularity)

# Adding title and labels
plt.title('Popularity of Programming Languages (Horizontal)')
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')

# Display the plot
plt.show()
