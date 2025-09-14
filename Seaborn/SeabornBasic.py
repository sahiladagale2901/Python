import seaborn as sns
import matplotlib.pyplot as plt

## Basic Plotting
tips = sns.load_dataset('tips')
print(tips.head())

### Scatter Plot
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title("Scatter -> Tips Plot")
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

### Line Plot
sns.lineplot(x='size', y='total_bill', data=tips)
plt.title("Line -> Tips Plot")
plt.show()

### Categorical Plots
### Bar Plots
sns.barplot(x='day', y='total_bill', data=tips)
plt.title("Bar -> Tips Plot")
plt.show()

### Box Plot
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title("Box -> Tips Plot")
plt.show()

### Violin Plot
sns.violinplot(x='day', y='total_bill', data=tips)
plt.title("Violin -> Tips Plot")
plt.show()

### Histogram Plot
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title("Histogram -> Tips Plot")
plt.show()

### KDE Plot
sns.kdeplot(tips['total_bill'], fill=True)
plt.title("KDE -> Tips Plot")
plt.show()

### Pair Plot
sns.pairplot(tips)
plt.show()

### Heat Map
corr = tips[['total_bill', 'tip', 'size']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Heat Map -> Tips Plot")
plt.show()
