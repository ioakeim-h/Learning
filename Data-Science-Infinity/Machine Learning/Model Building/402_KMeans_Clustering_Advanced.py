#################################################################
# KMeans Clustering - Advanced Template
#################################################################

# Libraries

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt

#################################################################
# Create the data
#################################################################

# Import tables

transactions = pd.read_excel("data/grocery_database.xlsx", sheet_name = "transactions")
product_areas = pd.read_excel("data/grocery_database.xlsx", sheet_name = "product_areas")

# Merge on product area name

transactions = pd.merge(transactions, product_areas, how = "inner", on = "product_area_id")

# Drop the non-food category

transactions.drop(transactions[transactions["product_area_name"] == "Non-Food"].index, inplace = True)

# Aggregate sales at customer level (by product area)

transaction_summary = transactions.groupby(["customer_id", "product_area_name"])["sales_cost"].sum().reset_index()

# Pivot data to place product areas as columns

transaction_summary_pivot = transactions.pivot_table(index = "customer_id",
                                                     columns = "product_area_name",
                                                     values = "sales_cost",
                                                     aggfunc = "sum",
                                                     fill_value = 0,
                                                     margins = True, 
                                                     margins_name = "Total").rename_axis(None, axis = 1)

# Turn sales into % sales

transaction_summary_pivot = transaction_summary_pivot.div(transaction_summary_pivot["Total"], axis = 0)

# Drop the "Total" column

data_for_clustering = transaction_summary_pivot.drop("Total", axis = 1)

#################################################################
# Data Preparation & Cleaning
#################################################################

# Check for missing values

data_for_clustering.isna().sum()

# Normalise data

scale_norm = MinMaxScaler()
data_for_clustering_scaled = pd.DataFrame(scale_norm.fit_transform(data_for_clustering), columns = data_for_clustering.columns)

#################################################################
# Use WCSS to find a good value for k
#################################################################

k_values = list(range(1,10))
wcss_list = []

for k in k_values:
    kmeans = KMeans(n_clusters = k, random_state = 42)
    kmeans.fit(data_for_clustering_scaled)
    wcss_list.append(kmeans.inertia_)

plt.plot(k_values, wcss_list)
plt.title("Within Cluster Sum of Squares - by k")
plt.xlabel("k")
plt.ylabel("WCSS Score")
plt.tight_layout()
plt.show()

#################################################################
# Instantiate & fit the model
#################################################################

kmeans = KMeans(n_clusters = 3, random_state = 42)
kmeans.fit(data_for_clustering_scaled)

#################################################################
# Use cluster information
#################################################################

# Add cluster labels to our data

data_for_clustering["cluster"] = kmeans.labels_

# Check cluster sizes

data_for_clustering["cluster"].value_counts()

#################################################################
# Profile our clusters
#################################################################

cluster_summary = data_for_clustering.groupby("cluster")[["Dairy", "Fruit", "Meat", "Vegetables"]].mean().reset_index()



