import webbrowser
import urllib.parse

# Replace with the movie name you're looking for
movie_name = "Inception"

# Format the movie name for URL encoding
movie_name_encoded = urllib.parse.quote(movie_name)

# Construct the search URL for Prime Video
url = f"https://www.primevideo.com/search/ref=atv_nb_sr?phrase={movie_name_encoded}"

# Open the URL in the default browser
webbrowser.open(url)

print(f"Searching for '{movie_name}' on Prime Video in your browser.")
