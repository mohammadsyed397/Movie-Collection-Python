menu_prompt = (
    "\nPlease choose an option:\n"
    "  a - Add a movie\n"
    "  l - List all movies\n"
    "  f - Find a movie\n"
    "  q - Quit the program\n"
    "Your choice: "
)

movies = []   # Empty movie list

# Function to add movies
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the director name: ")
    year = input("Enter the release year: ")

    movies.append({
        'title': title.strip(),
        'director': director.strip(),
        'year': year.strip()
    })
    print("\nMovie added successfully!\n")

# Function to display all movies
def show_movies():
    if not movies:
        print("\nNo movies in the collection.\n")
        return
    
    print("\n--- Movie Collection ---")
    for movie in movies:
        print_movie(movie)

# Function to print single movie
def print_movie(movie):
    print(f"Title    : {movie['title']}")
    print(f"Director : {movie['director']}")
    print(f"Year     : {movie['year']}")
    print("-" * 25)

# Function to find a movie
def find_movie():
    search_title = input("Enter the movie title to search: ").strip()

    for movie in movies:
        if movie['title'].lower() == search_title.lower():
            print("\nMovie Found:\n")
            print_movie(movie)
            return
    
    print("\nMovie not found.\n")

# Menu options dictionary
user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}

# Main menu function
def menu():
    selection = input(menu_prompt).lower().strip()
    while selection != 'q':
        if selection in user_options:
            user_options[selection]()
        else:
            print("\nInvalid option. Please try again.\n")

        selection = input(menu_prompt).lower().strip()

    print("\nGoodbye! Thank you for using Movie Manager.\n")

menu()
