# Movie Recommendation System

## Overview

The Movie Recommendation System is a Python-based project that recommends movies based on user-selected titles. It leverages datasets from TMDB (The Movie Database) to analyze movie attributes such as genres, keywords, cast, production companies, and crew, using Natural Language Processing (NLP) techniques to suggest similar titles.

## Features

- **Data Integration**: Combines movie details from two datasets: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
- **Data Cleaning and Extraction**: Processes the dataset to extract relevant information such as genres, keywords, cast, and crew names.
- **Tag Generation**: Creates a unique set of tags for each movie by combining multiple attributes.
- **Cosine Similarity**: Computes similarities between movie tags to identify similar films.
- **Recommendation Functionality**: Allows users to input a movie title and receive a list of recommended movies.

## Datasets

The datasets used for this project include:

1. **tmdb_5000_movies.csv**: Contains general movie information.
   - **Columns**: id, title, genres, keywords, overview, production_companies, production_countries, release_date

2. **tmdb_5000_credits.csv**: Contains information about the cast and crew of the movies.
   - **Columns**: title, cast, crew

## Installation

To run this project, ensure you have Python installed (preferably Python 3.6 or later). You will also need the following libraries:

- `numpy`
- `pandas`
- `nltk`
- `scikit-learn`

You can install these packages using pip:

```bash
pip install numpy pandas nltk scikit-learn
```


## Getting the Dataset

To download the Intel Image Classification dataset using the Kaggle API, follow these steps:

### Step 1: Set Up Kaggle API

1. **Create a Kaggle Account**:
   - If you haven't already, go to [Kaggle's website](https://www.kaggle.com/) and create an account.

2. **Get Your API Token**:
   - Log in to your Kaggle account.
   - Click on your profile picture in the top right corner and select **Account**.
   - Scroll down to the **API** section.
   - Click on **Create New API Token**. This action will download a file named `kaggle.json` to your computer.

### Step 2: Configure the Kaggle API

3. **Install the Kaggle Library**:
   Open your terminal or command prompt and install the Kaggle library if you haven't already:
   ```bash
   pip install kaggle
   ```

4. **Place the `kaggle.json` File**:
   - **For Windows**: Move the `kaggle.json` file to `C:\Users\<YourUsername>\.kaggle\`.
   - **For macOS/Linux**: Move it to `~/.kaggle/`.

   You can use the following commands to create the directory and move the file (assuming you're on macOS/Linux):
   ```bash
   mkdir -p ~/.kaggle
   mv /path/to/your/downloaded/kaggle.json ~/.kaggle/
   ```

5. **Set Permissions (macOS/Linux)**:
   Ensure that the `kaggle.json` file has the correct permissions so that it's secure:
   ```bash
   chmod 600 ~/.kaggle/kaggle.json
   ```

### Step 3: Download the Dataset

6. **Run the Download Command**:
   Use the following command in your terminal to download the Intel Image Classification dataset:
   ```bash
   kaggle datasets download -d puneet6060/intel-image-classification
   ```

7. **Unzip the Dataset**:
   The dataset will be downloaded as a zip file named `intel-image-classification.zip`. You need to unzip it. You can do this using the command line:

   For Linux or macOS:
   ```bash
   unzip intel-image-classification.zip
   ```

   For Windows, you can use the built-in file explorer to right-click on the zip file and select **Extract All**.

### Step 4: Load the Dataset in Your Code

After unzipping, you'll have the dataset files available in your current directory. You can now load the dataset using Pandas or any other library.

Here’s an example of how to load the data with Pandas if the dataset contains CSV files:

```python
import pandas as pd

# Replace 'filename.csv' with the actual name of the CSV file in the unzipped folder
df = pd.read_csv('filename.csv')
print(df.head())
```


