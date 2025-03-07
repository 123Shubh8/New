# -*- coding: utf-8 -*-
"""Sample_Sales_Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lXckycYHmVj2ju9Z7qksPRejbqDY9prB
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = './sales_data_sample.csv'
sales_data = pd.read_csv(file_path, encoding='ISO-8859-1')

sales_data.info()

sales_data.describe()

# Select relevant numerical columns for clustering
clustering_data = sales_data[['QUANTITYORDERED', 'PRICEEACH', 'SALES', 'MSRP']]

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(clustering_data)

# Using the elbow method to determine the optimal number of clusters
inertia = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=0, max_iter=100, n_init=5)  # Optimized parameters
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Plot the elbow method graph
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method to Determine Optimal Number of Clusters')
plt.show()

