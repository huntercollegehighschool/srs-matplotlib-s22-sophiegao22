"""
1. Import pyplot from matplotlib.
"""
import matplotlib.pyplot as plt

"""
2. Let's create a scatterplot to see if there are correlations bewteen age, height and weight. Run this three times, using two of the three lists each time.
plt.scatter(<x-values>, <y-values>)
"""

age = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
height = [2.3, 2.4, 2.5, 3, 3.2, 2.9, 4, 4.5, 4.3, 3.8, 5, 5.7]
weight = [6, 9, 10, 8, 7, 9, 12, 15, 18, 22, 19, 20]

one = plt.scatter(age, height)
two = plt.scatter(height, weight)
three = plt.scatter(weight, age)


"""
3. Have python display/show your graph.
"""
plt.show()
