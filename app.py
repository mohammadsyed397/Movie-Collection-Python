menu_prompt = "\n Enter a. to add a movie l.to list the movie collection f.to find the movies Q. to quit!!!"

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
    print(f"title:movie['title']")
    print(f"Director:movie['Director']")
    print(f"Year:movie['Year']")

#Function to find the movie 
def find_movie():
    search_title = input("Please Enter the movie title:")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)


def menu():
    selection = input(menu_prompt)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            show_movie()
        elif selection == 'f':
            find_movie()
        else:
            print("Please choose the option from the list below")
        selection = input(menu_prompt)
menu()



    