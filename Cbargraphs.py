"""
1. Import pyplot from matplotlib.
"""
import matplotlib.pyplot as plt


"""
2. Bar charts are the preferred way to display categorical data. Create a bar chart with the data below. Helpful code below:
plt.bar(<x-variables>, <y-values>)
"""

colors = ['red', 'yellow', 'green', 'blue']
counts = [6, 8, 7, 10]
plt.bar(colors, counts)


"""
3. Make python show/display the graph you created.
"""
plt.show()