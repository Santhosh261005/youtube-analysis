DAV Assignment_181

# YouTube Influencers Analysis with Python

## Overview
A basic data analysis project using Python's powerful libraries — **NumPy**, **Pandas**, and **Matplotlib** — to explore and visualize insights from a dataset of social media influencers on YouTube

---

## Getting Started

### Prerequisites
Make sure the following packages are installed:

- Python 3.x
- NumPy → `pip install numpy`
- Pandas → `pip install pandas`
- Matplotlib → `pip install matplotlib`

---

##  Operations Performed

### NumPy:
- **Array Creation:** `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`
- **Array Manipulation:** `.shape`, `.reshape()`, `np.concatenate()`, `np.split()`
- **Mathematical Operations:** `+`, `-`, `*`, `/`, `np.sqrt()`, `np.sin()`, `np.log()`
- **Universal Functions:** Element-wise computations
- **Aggregations:** `np.sum()`, `np.mean()`, `np.max()`, `np.min()`, etc.
- **Comparisons & Masking:** Boolean arrays and fancy indexing
- **Sorting:** `np.sort()`, `np.argsort()`
- **Structured Arrays:** Creation of compound types and record arrays

###  Pandas:
- **Data Loading & Inspection:** `read_csv()`, `head()`, `info()`, `describe()`
- **Selection & Indexing:** `df['col']`, `loc[]`, `iloc[]`, conditional filtering
- **Cleaning:** Handling missing values using `isnull()`, `fillna()`, and `dropna()`
- **Aggregation & Grouping:** `groupby()`, `mean()`, `sum()`, `value_counts()`
- **Combining Datasets:** `concat()`, `merge()`, `join()`
- **Pivot Tables & Hierarchical Indexing**
- **Handling Nulls and Index Alignments**

### Matplotlib:
- **Basic Plots:** `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.hist()`
- **Customization:** `title()`, `xlabel()`, `ylabel()`, `grid()`
- **Multiple Plots:** `subplot()`, `tight_layout()`
- **Save/Show:** `savefig()`, `show()`

---

## Dataset Description

The dataset `social media influencers - Youtube sep-2022.csv` contains detailed information about YouTube influencers including:

- **Rank** – Global influencer ranking  
- **Username** – Creator's name  
- **Subscribers** – Count of YouTube subscribers  
- **Country** – Country of the influencer  
- **Category** – Type of content (e.g., Entertainment, Education, etc.)  
- **Avg. Views** – Average views per video  
- **Engagement Rate** – Interaction level per video  
- **Authentic Engagement** – Verified audience engagement  
- **Total Videos** – Number of videos uploaded  
- **Channel Info** – Additional details  

---

## Key Findings (Example — update after your analysis)

- The dataset includes **[n] influencers** from **[x] countries**, across **[y] categories**.
- **Entertainment** is the most dominant category among top influencers.
- **Average subscriber count** varies significantly across categories.
- A positive correlation exists between **authentic engagement** and **subscriber count**.
- **Country-wise** comparison reveals emerging YouTube markets outside the US.
- **Histogram** shows how subscriber count is distributed across influencers.
- **Scatter plots** reveal potential outliers with high views but low engagement.

---

##  Insights from Visualizations

### 1. **Subscriber Distribution Histogram**
Helps identify whether the platform is dominated by mega-creators or has a broad spread of micro/mid-tier influencers.

### 2. **Subscribers vs. Engagement Rate Scatter Plot**
Detects patterns between influence and genuine audience connection.

### 3. **Top Categories Bar Chart**
Reveals the most popular content types on YouTube.

### 4. **Country-wise Analysis**
Shows YouTube’s global footprint and how user engagement varies by region.

---

##  Final Note

This project is a great starting point for:
- Practicing real-world data analysis.
- Understanding influencer dynamics.
- Gaining hands-on experience with data wrangling and visualization in Python.

Feel free to fork, explore, or expand this analysis with more advanced ML or dashboard tools like **Seaborn**, **Plotly**, or **Tableau**!




