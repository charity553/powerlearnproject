# 🧠 DATA ANALYSIS ASSIGNMENT
# Objective: Load, Analyze, and Visualize Dataset using Pandas & Matplotlib
# Dataset used: Iris Dataset (from sklearn)

# --- Import Required Libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set a style for prettier charts
sns.set(style="whitegrid")

# 🧩 TASK 1: LOAD AND EXPLORE THE DATASET

print("Loading the Iris dataset...")

try:
    # Load Iris dataset from sklearn
    iris_data = load_iris()
    df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
    print("Dataset successfully loaded!\n")

    # Display the first few rows
    print("🔹 First 5 rows of the dataset:")
    print(df.head(), "\n")

    # Check structure and data types
    print("🔹 Dataset Info:")
    print(df.info(), "\n")

    # Check for missing values
    print("🔹 Missing Values:")
    print(df.isnull().sum(), "\n")

    # Since Iris dataset has no missing data, let's show how we'd handle it
    # df.fillna(df.mean(), inplace=True)  # Example if data had missing values

except FileNotFoundError:
    print("❌ Error: Dataset file not found.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

# 📊 TASK 2: BASIC DATA ANALYSIS

print("Performing basic data analysis...\n")

# Basic statistics
print("🔹 Descriptive Statistics:")
print(df.describe(), "\n")

# Group by species and get average of numeric columns
grouped = df.groupby('species').mean()
print("🔹 Average Measurements by Species:")
print(grouped, "\n")

# Simple findings
print("🔍 Observations:")
print("- Iris-virginica generally has the largest petal and sepal measurements.")
print("- Iris-setosa has the smallest measurements overall.\n")

# 🎨 TASK 3: DATA VISUALIZATION

print("Creating visualizations...\n")

# --- 1. Line Chart: Average Petal Length per Species (trend) ---
plt.figure(figsize=(7,4))
plt.plot(grouped.index, grouped['petal length (cm)'], marker='o', color='teal')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.grid(True)
plt.show()

# --- 2. Bar Chart: Comparison of Average Sepal Width per Species ---
plt.figure(figsize=(7,4))
sns.barplot(x='species', y='sepal width (cm)', data=df, palette="viridis")
plt.title("Average Sepal Width per Species")
plt.xlabel("Species")
plt.ylabel("Sepal Width (cm)")
plt.show()

# --- 3. Histogram: Distribution of Petal Lengths ---
plt.figure(figsize=(7,4))
plt.hist(df['petal length (cm)'], bins=20, color='coral', edgecolor='black')
plt.title("Distribution of Petal Lengths")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# --- 4. Scatter Plot: Sepal Length vs Petal Length ---
plt.figure(figsize=(7,4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, s=70, palette='deep')
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()



print("Data Analysis Completed Successfully!\n")
print("Key Takeaways:")
print("• Iris-setosa species has smaller sepals and petals.")
print("• Iris-virginica species has the largest features.")
print("• Petal length and sepal length are positively correlated.")
print("• The dataset is clean, balanced, and ideal for classification problems.")
