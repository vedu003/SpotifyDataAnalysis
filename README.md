# Spotify Data Analysis Python Project 🎼🎧

This project contains exploratory data analysis (EDA) and visualizations of Spotify tracks and feature datasets. By utilizing Python's powerful data science libraries, we extract key insights regarding song popularity, duration, acoustic features, and genres over time.

---

## 📖 Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Requirements & Setup](#requirements--setup)
- [Dataset Details](#dataset-details)
- [Key Insights & Visualizations](#key-insights--visualizations)
- [How to Run](#how-to-run)

---

## 🔍 Project Overview
The goal of this project is to analyze music-related trends using Spotify datasets. The analysis covers:
1. Data cleansing and preprocessing (handling missing values, datatype conversions, and parsing dates).
2. Investigating correlation patterns between audio attributes (e.g., energy, loudness, acousticness).
3. Analyzing temporal trends such as the volume of song releases and change in song duration over the years.
4. Exploring genre-specific metrics to find the most popular genres and their audio profiles.

---

## 📁 Project Structure
```text
├── Data/
│   ├── tracks.csv               # Song tracks dataset (git-ignored)
│   └── SpotifyFeatures.csv      # Audio features dataset (git-ignored)
├── spotify.ipynb                # Interactive Jupyter Notebook analysis
├── spotify.py                   # Python script version of the analysis
├── .gitignore                   # Ignores local data files
└── README.md                    # Project documentation
```

---

## 🛠️ Requirements & Setup

### Prerequisites
Make sure you have **Python 3.x** installed. You will need the following libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`

### Installation
1. Install the required dependencies:
   ```bash
   pip install numpy pandas matplotlib seaborn
   ```
2. Create a folder named `Data/` in the project root directory.
3. Download the Spotify datasets and place them in the `Data/` folder as `tracks.csv` and `SpotifyFeatures.csv`.
   - *Dataset Source:* [Kaggle Spotify Dataset](https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets)

---

## 📊 Dataset Details
The project utilizes two main CSV datasets:
- **Tracks Dataset (`tracks.csv`)**: Contains general metadata of tracks including name, popularity, artists, release date, and duration.
- **Features Dataset (`SpotifyFeatures.csv`)**: Contains track metrics such as acousticness, danceability, energy, instrumentalness, liveness, valence, tempo, and genre categorization.

---

## 📈 Key Insights & Visualizations

### 1. Exploratory Data Analysis (EDA)
- **Data Overview**: Checking structure, column types, memory usage, and identifying null values.
- **Popularity Insights**: Identifying the 10 least popular and top 10 most popular songs in the dataset.
- **Descriptive Statistics**: Summary statistics for both tracks and features.

### 2. Preprocessing & Formatting
- **Release Date Indexing**: Converting release dates into unified datetime format and setting it as the primary index.
- **Duration Conversion**: Converting song durations from milliseconds to seconds.

### 3. Pearson Correlation Heatmap
- Visualizes the correlation matrix between different audio attributes (energy, loudness, acousticness, valence, etc.) to understand how different properties of music interrelate.

### 4. Regression Analysis
- **Loudness vs. Energy**: Shows a positive linear correlation between song energy and loudness.
- **Popularity vs. Acousticness**: Investigates how acousticness affects a track's popularity.

### 5. Songs Over the Years
- **Release Frequency**: A distribution plot showing the volume of songs released each year.
- **Duration Trends**: A line plot analyzing the evolution of average song duration over the years.

### 6. Genre Insights
- **Duration by Genre**: Comparing average track durations across different music genres.
- **Top 10 Genres by Popularity**: Visualizing the most popular genres based on track popularity scores.
- **Average Popularity by Genre**: Showing the overall average popularity profile per music genre.

### 7. Audio Attributes & Tempo Analysis
- **Tracks Popularity by Key & Mode**: Stripplot mapping the track popularity across different keys and modes.
- **Tempo vs. Popularity**: KDE density plot visualizing the distribution of popularity across different tempos.

---

## 🚀 How to Run

### Interactive Notebook
Open and run all cells in [spotify.ipynb](file:///f:/SpotifyDataAnalysis/spotify.ipynb) using Jupyter Notebook or VS Code:
```bash
jupyter notebook spotify.ipynb
```

### Python Script
Run the script-based implementation directly in your terminal:
```bash
python spotify.py
```
*Note: The script outputs descriptive print statements and displays the generated plots sequentially.*
