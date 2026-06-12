import json 

with open("books.json", "r") as f:
    books = json.load(f)

def get_published_fantasy(books):
    # Return a list of book titles that are 
    # both fantasy genre AND published status
    fantasy_status = []
    for book in books: 
        if book["genre"] == "fantasy" and book["status"] == "published" :
            fantasy_status.append(book["book"])
    return fantasy_status

 
get_published_fantasy(books)

def get_average_rating_by_genre(books):
# Return average rating per genre
    # rounded to 2 decimal places
    # {"fantasy": 4.75, "romance": ..., "thriller": ...}
    book_genre_average = {}
    book_count = {}
    for book in books: 
        genre = book["genre"]
        rating = book["rating"]
        if genre not in book_genre_average:
            book_genre_average[genre] = 0
        book_genre_average[genre] += rating
    
    for book in books:
        genre = book["genre"]
        if genre not in book_count:
            book_count[genre] = 0
        book_count[genre] += 1
    
    result = {}
    for genre in book_genre_average:
        result[genre] = round(book_genre_average[genre] / book_count[genre] , 2)
    return result

print(get_average_rating_by_genre(books))

def get_highest_rated_book(books):

# Return the title of the highest rated book
    # regardless of status
    highest_rated = ""
    rating = 0 
    for book in books: 
        if book["rating"] > rating:
            rating = book["rating"]
            highest_rated = book["book"]
    return highest_rated

print(get_highest_rated_book(books))

def get_books_by_year(books):
    book_by_year = {}
# Group book titles by year published
    # {"2021": ["The Midnight Crown", "The Last Cartographer"], ...}
    for book in books:
        year = book["year"]
        title = book["book"]
        if year not in book_by_year:
            book_by_year[year] = []
        book_by_year[year].append(title)
    return book_by_year

print(get_books_by_year(books))