import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

print("line plot:\n")
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

print("\nCreate customized plot:\n")
plt.plot(x, y, color='red', linestyle='-.')
plt.show()
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.show()
plt.plot(x, y, color='red', linestyle='--', marker='o', linewidth='3', markersize=9)
plt.grid(True)
plt.show()

print("\n################ Multiple plot:\n")

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.figure(figsize=(9, 5))

# its means 1 row 2 column and position is 1 (1:2:1)
plt.subplot(1, 2, 2)
plt.plot(x, y1, color='green')
plt.title("Plot 1")

plt.subplot(1, 2, 1)
plt.plot(x, y2, color='red')
plt.title("Plot 2")
plt.show()

print("\n################ Bar plot:\n")

cat = ['A', 'B', 'C', 'D', 'E']
values = [5, 6, 7, 8, 4]

plt.bar(cat, values, color='blue')
plt.show()

print("\n################ Histogram plot:\n")

data = [1, 2, 3, 4, 3, 5, 6, 5, 4, 3, 2, 4, 6, 8, 5, 9, 0, 5, 5, 3]
plt.hist(data, bins=10, color='orange', edgecolor='black')
plt.show()

print("\n################ Scatter plot:\n")

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 1, 4, 5, 7, 8, 9, 5]

plt.scatter(x, y, color='red', marker='.')
plt.show()

print("\n################ Scatter plot with customize length:\n")
y = [2, 1, 4, 5, 7, 8, 9, 5, 1, 4, 5, 7, 8, 9, 5]
x = list(range(1, len(y) + 1))  # auto-generate x = [1,2,...,15]

# Scatter with size proportional to y
plt.scatter(x, y, color='red', marker='.')
plt.show()

print("\n################ Pie chart:\n")

labels = ['a', 'b', 'c', 'd']
size = [30, 30, 20, 10]
color = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(size, labels=labels, colors=color, autopct='%1.1f%%', shadow=True)
plt.show()

# Move out the 1st slice
explode = (0.2, 0, 0, 0)
plt.pie(size, explode=explode, labels=labels, colors=color, autopct='%1.1f%%', shadow=True)
plt.show()
