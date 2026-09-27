
import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# LOAD SAVED DATA
# -----------------------------

@st.cache_resource
def load_data():

    with open("movies.pkl", "rb") as file:
        movies = pickle.load(file)

    with open("similarity.pkl", "rb") as file:
        similarity = pickle.load(file)

    return movies, similarity


data, similarity = load_data()

# -----------------------------
# RECOMMENDATION FUNCTION
# -----------------------------

def recommend(movie):

    movie_index = data[
        data["title"].str.lower() == movie.lower()
    ].index

    if len(movie_index) == 0:
        return []

    movie_index = movie_index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:

        movie_name = data.iloc[i[0]]["title"]
        homepage = data.iloc[i[0]]["homepage"]
        score = float(i[1])

        # Handle missing homepage URLs
        if pd.isna(homepage) or not str(homepage).strip():
            homepage = None

        recommendations.append({
            "title": movie_name,
            "homepage": homepage,
            "score": score
        })

    return recommendations


# -----------------------------
# STREAMLIT UI
# -----------------------------

st.title("🎬 Movie Recommendation System")

st.write(
    "Find movies similar to your favourite movie "
    "using Machine Learning and Cosine Similarity."
)

st.divider()

# Movie selection
movie_list = data["title"].dropna().unique().tolist()

selected_movie = st.selectbox(
    "Select a movie",
    movie_list,
    index=None,
    placeholder="Search or select a movie..."
)

# Recommendation button
if st.button("Recommend Movies", type="primary"):

    if selected_movie is None:

        st.warning("Please select a movie first.")

    else:

        recommendations = recommend(selected_movie)

        if recommendations:

            st.subheader(
                f"Movies similar to {selected_movie}"
            )

            # Display recommendations
            for index, movie in enumerate(
                recommendations, start=1
            ):

                with st.container(border=True):

                    st.markdown(
                        f"### {index}. {movie['title']}"
                    )

                    st.write(
                        f"Similarity Score: "
                        f"{movie['score']:.2%}"
                    )

                    if movie["homepage"]:

                        st.link_button(
                            "Visit Movie Homepage",
                            movie["homepage"]
                        )

                    else:

                        st.caption(
                            "Official homepage not available."
                        )

        else:

            st.error("Movie not found in the dataset.")

st.divider()

st.caption(
    "Built with Python, Pandas, Scikit-learn and Streamlit"
)