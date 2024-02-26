import matplotlib.pyplot as plt
import pandas as pd

def visualize_column(df, column_name):
    # Get's the dtype of column
    dtype = df[column_name].dtype

    # Determine the type of plot based on the dtype
    if dtype == 'int64' or dtype == 'float64':
        # Numeric data: Create a histogram
        plt.figure(figsize=(8, 6))
        plt.hist(df[column_name], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Histogram of {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.show()
    elif dtype == 'object' or dtype == 'bool':
        # Categorical data: Create a bar chart
        value_counts = df[column_name].value_counts()
        plt.figure(figsize=(8, 6))
        value_counts.plot(kind='bar', color='lightcoral')
        plt.title(f'Bar Chart of {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()
    else:
        print(f"Data type {dtype} is not avaliable for visualization. Coming soon!")