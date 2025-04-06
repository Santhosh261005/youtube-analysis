import pandas as pd
import numpy as np

# Load and clean dataset
df = pd.read_csv("social media influencers - Youtube sep-2022.csv")

# Strip spaces from column names
df.columns = df.columns.str.strip()

# Check columns once (optional)
print("Columns:", df.columns)

# Continue processing
df['Subscribers'] = df['Subscribers'].str.replace('M', '').astype(float)
subs_array = df['Subscribers'].values


# --- NumPy UNIT-I ---

# Data type
print("Data type:", subs_array.dtype)

# Creating arrays, indexing, slicing
arr = np.arange(10)
print("Array:", arr)
print("Slice:", arr[2:7])

# Reshape, concatenate, split
reshaped = arr.reshape(2, 5)
concat = np.concatenate([arr[:5], arr[5:]])
split1, split2 = np.split(arr, [5])
print("Reshaped:\n", reshaped)
print("Concat:", concat)
print("Split:", split1, split2)

# Universal functions, aggregation
print("Mean:", np.mean(subs_array))
print("Max:", np.max(subs_array))
print("Sqrt:", np.sqrt(subs_array))

# Broadcasting
boosted = subs_array + 10
print("Boosted subs:", boosted[:5])

# Boolean masks
mask = subs_array > 100
print("High subs:\n", df[mask])

# Fancy indexing
print("Fancy indexing:", subs_array[[0, 2, 4]])

# Sorting
print("Sorted subs:", np.sort(subs_array))
print("Argsorted:", np.argsort(subs_array))

# Structured arrays
structured = np.array(list(zip(df['Name'], subs_array)), dtype=[('name', 'U50'), ('subs', 'f8')])
print("Structured:\n", structured[:3])

# --- Pandas UNIT-II ---

# Series and DataFrames
series = pd.Series(subs_array)
print("Series:\n", series.head())

# Indexing
print("iloc:", df.iloc[0])
print("loc:", df.loc[0])
print("Country column:\n", df['Country'].head())

# Index alignment
df['Boosted_Subs'] = subs_array + 5

# Handling missing data
print("Nulls:\n", df.isnull().sum())
df_filled = df.fillna("Unknown")

# Hierarchical indexing
df.set_index(['Country', 'Category_2'], inplace=True)
print("Hierarchical Index:\n", df.head())

# Reset index to continue with UNIT-III
df.reset_index(inplace=True)

# --- UNIT-III ---

# Merge example
dummy_df = pd.DataFrame({
    'Name': ['T-Series', 'PewDiePie'],
    'Founded_Year': [2006, 2010]
})
merged = pd.merge(df, dummy_df, on='Name', how='left')
print("Merged:\n", merged[['Name', 'Founded_Year']].head())

# Aggregation
grouped = df.groupby('Country')['Subscribers'].count()
print("Grouped by Country:\n", grouped.head())

# Pivot table
pivot = df.pivot_table(values='Boosted_Subs', index='Country', aggfunc='mean')
print("Pivot Table:\n", pivot.head())



# 1. Histogram: Distribution of Subscriber Counts
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.hist(df['Subscribers'], bins=20, edgecolor='black')
plt.title('Distribution of Subscribers (in Millions)')
plt.xlabel('Subscribers (Millions)')
plt.ylabel('Number of Influencers')
plt.grid(True)
plt.show()

# 2. Scatter Plot: Subscribers vs Video Views
# Clean 'Video Views' column if required (remove commas and convert to float)
df['Video Views'] = df['Video Views'].astype(str).str.replace(',', '')
df['Video Views'] = pd.to_numeric(df['Video Views'], errors='coerce')

plt.figure(figsize=(8, 6))
plt.scatter(df['Subscribers'], df['Video Views'], alpha=0.7)
plt.title('Subscribers vs. Video Views')
plt.xlabel('Subscribers (Millions)')
plt.ylabel('Video Views')
plt.grid(True)
plt.show()

#3. Bar Plot: Number of Influencers per Country
country_counts = df['Country'].value_counts().head(15)  # Top 15 countries

plt.figure(figsize=(10, 6))
country_counts.plot(kind='bar', edgecolor='black')
plt.title('Top 15 Countries by Number of Influencers')
plt.xlabel('Country')
plt.ylabel('Number of Influencers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
