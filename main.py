import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("fruit_dataset.csv")

# Set up the plot area
plt.figure(figsize=(20, 20))

# 1. Bar plot: Fruit count
plt.subplot(3, 3, 1)
df['Fruit'].value_counts().plot(kind='bar')
plt.title('Fruit Count')
plt.xlabel('Fruit')
plt.ylabel('Count')

# 2. Pie chart: Origin distribution
plt.subplot(3, 3, 2)
df['Origin'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Origin Distribution')
plt.ylabel('')

# 3. Histogram: Quantity distribution
plt.subplot(3, 3, 3)
plt.hist(df['Quantity'], bins=20, edgecolor='black')
plt.title('Quantity Distribution')
plt.xlabel('Quantity')
plt.ylabel('Frequency')

# 4. Box plot: Price per unit by fruit
plt.subplot(3, 3, 4)
df.boxplot(column='Price_per_Unit', by='Fruit', grid=False)
plt.title('Price per Unit by Fruit')
plt.suptitle('')  # Remove the default title
plt.xlabel('Fruit')
plt.ylabel('Price per Unit')

# 5. Scatter plot: Quantity vs Total Price
plt.subplot(3, 3, 5)
plt.scatter(df['Quantity'], df['Total_Price'], alpha=0.5)
plt.title('Quantity vs Total Price')
plt.xlabel('Quantity')
plt.ylabel('Total Price')

# 6. Bar plot: Average price per fruit
plt.subplot(3, 3, 6)
avg_price = df.groupby('Fruit')['Price_per_Unit'].mean()
avg_price.plot(kind='bar')
plt.title('Average Price per Fruit')
plt.xlabel('Fruit')
plt.ylabel('Avg Price')

# 7. Horizontal bar chart: Fruit color count
plt.subplot(3, 3, 7)
df['Color'].value_counts().plot(kind='barh')
plt.title('Fruit Color Count')
plt.xlabel('Count')
plt.ylabel('Color')

# 8. Line plot: Sorted Quantity
plt.subplot(3, 3, 8)
sorted_quantities = df['Quantity'].sort_values().reset_index(drop=True)
plt.plot(sorted_quantities)
plt.title('Sorted Quantity')
plt.xlabel('Index')
plt.ylabel('Quantity')

# 9. Area plot: Total price per fruit (cumulative)
plt.subplot(3, 3, 9)
total_by_fruit = df.groupby('Fruit')['Total_Price'].sum().sort_values()
plt.fill_between(range(len(total_by_fruit)), total_by_fruit)
plt.xticks(ticks=range(len(total_by_fruit)), labels=total_by_fruit.index, rotation=45)
plt.title('Total Price per Fruit')
plt.xlabel('Fruit')
plt.ylabel('Total Price')

# Adjust layout
plt.tight_layout()
plt.show()

