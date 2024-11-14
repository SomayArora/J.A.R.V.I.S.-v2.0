import webbrowser

# Dictionary mapping genres to their IMDb genre codes (as a simple example)
genres = {
    'action': 'action',
    'adventure': 'adventure',
    'animation': 'animation',
    'biography': 'biography',
    'comedy': 'comedy',
    'crime': 'crime',
    'documentary': 'documentary',
    'drama': 'drama',
    'family': 'family',
    'fantasy': 'fantasy',
    'film-noir': 'film_noir',
    'game-show': 'game_show',
    'history': 'history',
    'horror': 'horror',
    'music': 'music',
    'musical': 'musical',
    'mystery': 'mystery',
    'news': 'news',
    'reality': 'reality',
    'romance': 'romance',
    'sci': 'Sci-Fi',
    'sitcom': 'sitcom',
    'sport': 'sport',
    'talk-show': 'talk_show',
    'thriller': 'thriller',
    'war': 'war',
    'western': 'western'
}

# Show available genres
print("Available genres: action, adventure, animation, biography, comedy, crime, documentary, drama, family, fantasy, film-noir, game-show, history, horror, music, musical, mystery, news, reality, romance, sci, sitcom, sport, talk-show, thriller, war, western")

# Get the genre from the user input
genre = input("Enter movie type: ").lower()

# Check if the genre is valid and open the IMDb search URL
if genre in genres:
    imdb_url = f"https://www.imdb.com/search/title/?genres={genres[genre]}"
    webbrowser.open(imdb_url)
else:
    print("Invalid genre entered. Opening IMDb homepage.")
    webbrowser.open('https://www.imdb.com')
