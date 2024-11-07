# Movie Recommender System

This is an interactive **Movie Recommender System** built with **Streamlit** that allows users to receive personalized movie recommendations based on their selected movie. The system leverages a similarity model and fetches movie posters using **The Movie Database (TMDb) API**.

---

## Features:

- **Movie Selection**: Users can type in or select a movie from a dropdown list.
- **Recommendations**: After selecting a movie, the system recommends 5 similar movies.
- **Movie Posters**: The posters for the recommended movies are fetched from The Movie Database (TMDb) API.
- **User Interface**: Simple and intuitive interface built using Streamlit.
  
---

## Technical Stack:

- **Streamlit**: Front-end library for creating interactive applications.
- **Pandas**: For data manipulation and handling of movie metadata.
- **Pickle**: For loading pre-trained models (movie data and similarity matrix).
- **Requests**: For making API requests to fetch movie posters.
- **The Movie Database (TMDb) API**: For fetching movie posters.

---

## Installation

To run this project locally, follow the steps below:

### Prerequisites:

- Python 3.x
- pip (Python package installer)

### 1. Clone the Repository:

bash
git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system
2. Install Dependencies:
Use requirements.txt to install the required libraries.

bash
Copy code
pip install -r requirements.txt
Alternatively, you can install the individual libraries using pip:

bash
Copy code
pip install streamlit pandas requests
3. Set Up TMDb API Key:
Go to TMDb API and sign up for an API key.
Replace the YOUR_API_KEY placeholder in the code with your actual API key in the app.py file.
Running the Application:
To run the Streamlit app locally:

bash
Copy code
streamlit run app.py
This will launch the app in your web browser, where you can interact with the Movie Recommender System.

How it Works:
Movie Selection: When you run the app, you can select a movie from a dropdown list of available movies.
Recommendation Process: Upon selecting a movie, the system calculates the similarity between the chosen movie and others, using the pre-trained similarity matrix.
Posters and Movie Information: The top 5 similar movies are recommended along with their posters, fetched from The Movie Database (TMDb) API.
Interface: The user-friendly interface displays the recommended movies in a visually appealing layout.
Files:
app.py: The main Streamlit application code.
movie_dict.pkl: A pickle file containing movie metadata (e.g., movie titles and IDs).
similarity.pkl: A pickle file containing the similarity matrix used to recommend similar movies.
requirements.txt: A text file listing all dependencies required to run the app.
Future Improvements:
User Feedback: Allow users to provide ratings for the recommendations, enabling the system to learn and improve over time.
Enhanced Recommendations: Integrate additional features like genre, director, or actor data for more accurate recommendations.
Recommendation History: Store user preferences or past recommendations for personalized suggestions.
