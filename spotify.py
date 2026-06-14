import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Datasets
sp_tracks = pd.read_csv('Data/tracks.csv')
sp_feature = pd.read_csv('Data/SpotifyFeatures.csv')

# 2. Explore the Datasets
# Viewing the tracks data
print("Tracks Data Head:")
print(sp_tracks.head())

# Viewing the feature data
print("\nFeatures Data Head:")
print(sp_feature.head())

# Checking null values
print("\nNull Values in Tracks:")
print(sp_isnull_tracks := pd.isnull(sp_tracks).sum())

print("\nNull Values in Features:")
print(sp_isnull_feature := pd.isnull(sp_feature).sum())

# Checking info
print("\nTracks Dataset Info:")
sp_tracks.info()

print("\nFeatures Dataset Info:")
sp_feature.info()

# Finding 10 least popular songs in the Spotify dataset
print("\n10 Least Popular Songs:")
least_popular = sp_tracks.sort_values('popularity', ascending=True)[0:10]
print(least_popular[['name', 'popularity']])

# Descriptive statistics of tracks
print("\nTracks Descriptive Statistics:")
print(sp_tracks.describe().transpose())

# Descriptive statistics of features
print("\nFeatures Descriptive Statistics:")
print(sp_feature.describe().transpose())

# Finding top 10 popular songs in the Spotify dataset
print("\nTop 10 Popular Songs:")
top_popular = sp_tracks[sp_tracks['popularity'] > 90].sort_values('popularity', ascending=False)[:10]
print(top_popular[['name', 'popularity', 'artists']])

# 3. Data Cleansing & Transformation
# Make the Release Date Column as the Index Column
sp_tracks['release_date'] = pd.to_datetime(
    sp_tracks['release_date'],
    format='mixed'
)
sp_tracks.set_index('release_date', inplace=True)
sp_tracks.index = pd.to_datetime(sp_tracks.index)
print("\nTracks Data Head with Release Date Index:")
print(sp_tracks.head())

# Find the Name of the Artist Present in the 18th Row of the Dataset
print("\nArtist in the 18th row:")
print(sp_tracks[['artists']].iloc[18])

# Convert the Duration of the Songs From Milliseconds to Seconds
sp_tracks['duration'] = sp_tracks['duration_ms'].apply(lambda x : round(x/1000))
sp_tracks.drop('duration_ms', inplace=True, axis=1)
print("\nTracks Duration Head (in seconds):")
print(sp_tracks.duration.head())

# 4. Correlation Analysis
# Correlation HeatMap using Pearson Correlation method between variables
td = sp_tracks.drop(['id', 'name', 'artists', 'id_artists'], axis=1).corr(method='pearson')
plt.figure(figsize=(9, 5))
hmap = sns.heatmap(td, annot=True, fmt='.1g', vmin=-1, vmax=1, center=0, cmap='Greens', linewidths=0.1, linecolor='black')
hmap.set_title('Correlation HeatMap')
hmap.set_xticklabels(hmap.get_xticklabels(), rotation=90)
plt.tight_layout()
plt.show()

# 5. Regression Analysis
# Sample Only 0.4 Percent of the Whole Dataset (represented as 0.004)
sample_sp = sp_tracks.sample(int(0.004 * len(sp_tracks)))
print(f"\nSample size: {len(sample_sp)}")

# Create a Regression Plot Between Loudness and Energy
plt.figure(figsize=(8, 4))
sns.regplot(
    data=sample_sp,
    x='energy',
    y='loudness',
    scatter_kws={'color': 'green'},
    line_kws={'color': 'red'}
)
plt.title('Regression Plot - Loudness vs Energy Correlation')
plt.tight_layout()
plt.show()

# Create a Regression Plot Between Popularity and Acousticness
plt.figure(figsize=(8, 4))
sns.regplot(
    data=sample_sp,
    x='acousticness',
    y='popularity',
    scatter_kws={'color': 'green'},
    line_kws={'color': 'red'}
)
plt.title('Regression Plot - Popularity vs Acousticness Correlation')
plt.tight_layout()
plt.show()

# 6. Songs per Year Analysis
# Creating new column in tracks table
sp_tracks['dates'] = sp_tracks.index.get_level_values('release_date')
sp_tracks.dates = pd.to_datetime(sp_tracks.dates)
years = sp_tracks.dates.dt.year

sns.displot(years, discrete=True, aspect=2, height=4, kind='hist', color='g').set(title='No of songs - per year')
plt.tight_layout()
plt.show()

# 7. Year vs Duration Analysis (Line Plot)
total_dr = sp_tracks['duration']
sns.set_style(style="whitegrid")
plt.figure(figsize=(11, 6))
sns.lineplot(x=years, y=total_dr).set(title="Year vs Duration")
plt.xlabel('Dates')
plt.ylabel('Duration')
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

# 8. Genre and Popularity Analysis (Spotify Features)
# Plot Duration of the Songs w.r.t. different Genres using a horizontal barplot
plt.figure(figsize=(10, 6))
plt.title('Duration of songs in different Genres')
sns.color_palette('crest', as_cmap=True)
sns.barplot(y='genre', x='duration_ms', data=sp_feature)
plt.xlabel('Duration in ms')
plt.ylabel('Genres')
plt.tight_layout()
plt.show()

# Find top genres by Popularity and plot a barplot
sns.set_style(style="darkgrid")
plt.figure(figsize=(10, 5))
famous = sp_feature.sort_values("popularity", ascending=False).head(10)
sns.barplot(y='genre', x='popularity', data=famous).set(title="Top 5 Genres by Popularity")
plt.tight_layout()
plt.show()

# Average Popularity by Genre
avg_popularity_by_genre = sp_feature.groupby('genre')['popularity'].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 6))  
sns.barplot(x=avg_popularity_by_genre.index, y=avg_popularity_by_genre.values, palette="rocket")
plt.xlabel("Genre") 
plt.ylabel("Average Popularity")  
plt.title("Average Popularity by Genre")
plt.xticks(range(len(avg_popularity_by_genre.index)), rotation=90)  
plt.tight_layout()
plt.show()

# Strip Plot: Tracks popularity by Key and Mode
same_df_low_sample = sp_feature.sample(1000)
sns.set_style('darkgrid')
fig, ax = plt.subplots(figsize=(10, 6))
sns.stripplot(data=same_df_low_sample, x='key', y='popularity', palette='icefire', hue='mode')
ax.set_title('Tracks Popularity by Key & Mode')
plt.tight_layout()
plt.show()

# KDE Plot: Popularity according to Tempo
sns.set_style('whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=sp_feature, x='tempo', y='popularity', fill=True, cmap="viridis")
ax.set_title('Popularity according to tempo')
plt.tight_layout()
plt.show()
