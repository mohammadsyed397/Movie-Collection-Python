menu_prompt = (
    "\nPlease choose an option:\n"
    "  a - Add a movie\n"
    "  l - List all movies\n"
    "  f - Find a movie\n"
    "  q - Quit the program\n"
    "Your choice: "
)


movies = [] # Empty moive List

# Function to add movies into list
def add_movie():
    title = input("Please Enter the movie title:")
    Director = input("Please Enter the Director Name:")
    Year = input("Please Enter the Year:")
    movies.append({
        'title': title,
        'Director': Director,
        'Year': Year
    })

#Function to show movie information 
def show_movie():
    for movie in movies:
        print_movie(movie)

#Function to print movie information
def print_movie(movie):
    print(f"title:{movie['title']}")
    print(f"Director:{movie['Director']}")
    print(f"Year:{movie['Year']}")

#Function to find the movie 
def find_movie():
    search_title = input("Please Enter the movie title:")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)


user_options = {
    "a": add_movie,
    "l": show_movie,
    "f": find_movie
}


def menu():
    selection = input(menu_prompt)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(menu_prompt)


menu()