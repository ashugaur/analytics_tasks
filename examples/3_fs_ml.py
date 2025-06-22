# %% File search ML (KMeans)

## Dependencies
from pathlib import Path
import polars as pl
from analytics_tasks.file_search.build import lib_refs
from analytics_tasks.ml.functions.info_schema_parser import info_schema_parser
from analytics_tasks.utils import fakedatagenerator as fdg
from analytics_tasks.file_search.functions import load_fs_polars

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

## Project folder (at_dir: analytics_tasks directoary)
at_dir = Path("C:/my_disk/____tmp/analytics_tasks")


## Assign file/folder references
fs_index_dir, logs_folder, time_machine, reports_folder = lib_refs(at_dir)


# %% Data (SQL file corpus)

## Load file search index
searchx = load_fs_polars(fs_index_dir)
searchx_sql = searchx.filter(pl.col("ext") == ".sql").unique()

## Information schema parser
generator = fdg.FakeDataGenerator()
info_schema_df = generator.generate_fake_info_schema(num_rows=50)
info_schema_parsed = info_schema_parser(searchx_sql, info_schema_df)
info_schema_parsed["HashTags"].unique().head().to_list()


## File + Derived HashTags (Info schema names)
df = info_schema_parsed["unc", "HashTags"].unique().to_pandas()
print(df[:5])


# %% Encoding

## Store to lists
hash_list = df["HashTags"].tolist()
title_list = df["unc"].tolist()
print(hash_list[0:3])


## TF-IDF conversion
vectorizer = TfidfVectorizer(stop_words="english")
hash_matrix = vectorizer.fit_transform(hash_list)
print("Feature names Identified:")
print(vectorizer.get_feature_names_out())


# %% Model: KMeans

## Split data
kmeans = KMeans(n_clusters=6).fit(hash_matrix)
kmeans


## Cluster labels
clusters = kmeans.labels_
print(clusters[0:10])


## Cluster members
for group in set(clusters):
    print("\nGroup:", group, "\n-------------------")
    for i in df.index:
        if (clusters[i] == group) & (i <= 5):
            print(title_list[i])


# %% Optimal Cluster size

## Sum of squared distances
sosd = []

## Run clustering for sizes 1 to 15 and capture inertia
K = range(1, 15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(hash_matrix)
    sosd.append(km.inertia_)
print("Sum of squared distances : ", sosd)


## Plot sosd against number of clusters
plt.plot(K, sosd, "bx-")
plt.xlabel("Cluster count")
plt.ylabel("Sum_of_squared_distances")
plt.title("Elbow Method For Optimal Cluster Size")
plt.show()


## Score
df["clusters"] = clusters
print(df.head())


## % of files in each cluster
print("% of files in each cluster")
df.clusters.value_counts(normalize=True) * 100


## Use cases
""" Manually tag the cluster groups to classify files into named categories.

    Use the classified index to:
        Organize the SQL (in this case) files into categories for easy access.
        Create data table with links to SQL code for quick reference.
        Create MkDocs site with the SQL code for quick reference.
        Extract pieces of code from relevenat SQL files for quick reference.
        Finetune LLM using the filtered output as embeddings.
        Create functions on classified index for precise search.
"""
