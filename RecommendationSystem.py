print("Movie Recommendation System")

movies = {
    "Action": ["Leo", "Vikram", "Master"],
    "Comedy": ["Boss Engira Baskaran", "OK OK", "Kalakalappu"],
    "Romance": ["96", "Sita Ramam", "Love Today"],
    "Horror": ["Demonte Colony", "Pizza", "Yaavarum Nalam"]
}

print("\nAvailable Genres:")
for genre in movies:
    print("-", genre)

choice = input("\nEnter your favorite genre: ")

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print(movie)
else:
    print("Sorry, genre not found.")
