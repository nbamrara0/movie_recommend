
# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Python, Pandas, NLP, and Machine Learning techniques. This project recommends movies similar to a movie selected by the user based on movie content such as genres, cast, crew, and tags.

##  Project Overview

The Movie Recommendation System analyzes movie information and recommends similar movies using Natural Language Processing (NLP) and Cosine Similarity.

The system processes movie data, converts textual information into numerical vectors, and calculates similarity between movies to generate recommendations.

##  Features

- Movie data preprocessing and cleaning
- Text tokenization and stemming
- Feature extraction from genres, cast, crew, and tags
- Text vectorization using CountVectorizer
- Cosine Similarity to measure movie similarity
- Recommends similar movies based on user input

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| NLTK | NLP and stemming |
| Scikit-learn | Vectorization and similarity calculation |
| Jupyter Notebook | Model development and experimentation |

##  Project Structure

```text
movie_recomanded/
│
├── NEW.IPYNB
├── workdata_clean.csv
├── README.md
└── requirements.txt
```

##  Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nbamara0/movie_recomend.git
```

### 2. Navigate to the Project Folder

```bash
cd movie_recomend
```

### 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn nltk jupyter
```

### 4. Run Jupyter Notebook

```bash
jupyter notebook
```

Open `NEW.IPYNB` and run the notebook cells.

## How It Works

1. Data Collection: Load the movie dataset containing movie titles, genres, cast, crew, and tags.

2. Data Preprocessing: Clean missing values, handle duplicates, and prepare text features.

3. Tokenization: Split movie descriptions and other text features into individual tokens.

4. Stemming: Reduce words to their root forms to normalize textual data.

5. Feature Engineering: Combine relevant movie features into a single text representation.

6. Vectorization: Convert text into numerical vectors using CountVectorizer.

7. Similarity Calculation: Calculate Cosine Similarity between movie vectors.

8. Recommendation: Find movies with the highest similarity scores and display the recommended movie titles and homepage URL.

##  Machine Learning Approach

This project uses Content-Based Filtering.

Unlike collaborative filtering, which depends on user ratings and preferences from other users, content-based filtering recommends movies based on similarities in their features.

Cosine Similarity is used to measure the similarity between movie vectors.

## Future Improvements

- Develop a web application using Flask or FastAPI.
- Create a movie search interface.
- Display movie posters and details using a movie database API.
- Store user watch history and preferences.
- Build personalized recommendations based on user activity.
- Deploy the application to a cloud platform.

## Author

**Naveen chandra Bamrara**

Python Developer | Machine Learning Enthusiast

GitHub: [nbamara0](https://github.com/nbamara0)

---

⭐ If you find this project useful, consider giving it a star!
