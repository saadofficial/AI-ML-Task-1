# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
iris = sns.load_dataset("iris")

# Print shape of dataset
print("Shape of Dataset:")
print(iris.shape)

# Print column names
print("\nColumn Names:")
print(iris.columns)

# Print first 5 rows
print("\nFirst 5 Rows:")
print(iris.head())

# Dataset information
print("\nDataset Info:")
print(iris.info())

# Summary statistics
print("\nSummary Statistics:")
print(iris.describe())

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(
    x="sepal_length",
    y="sepal_width",
    hue="species",
    data=iris
)

plt.title("Sepal Length vs Sepal Width")
plt.show()

# -----------------------------
# Histograms
# -----------------------------
iris.hist(figsize=(10,8))
plt.suptitle("Histograms of Iris Dataset")
plt.show()

# -----------------------------
# Box Plots
# -----------------------------
plt.figure(figsize=(10,6))

sns.boxplot(data=iris)

plt.title("Box Plot of Iris Dataset")
plt.show()