import pytest

from books import books, get_published_fantasy, get_average_rating_by_genre, get_highest_rated_book, get_books_by_year

def test_fantasy_published():
    result = get_published_fantasy(books)
    assert "The Midnight Crown" in result

def test_average_genre_rating():
    result = get_average_rating_by_genre(books)
    assert 4.75 == result["fantasy"]
    assert 4.17 == result["romance"]
    assert 4.13 == result["thriller"]

def test_hihest_rated_book():
    result = get_highest_rated_book(books)
    assert "Veilborn" in result 

def test_books_by_year():
    result = get_books_by_year(books)
    assert "The Last Cartographer" in result[2021]
    assert "Salt and Ember" in result[2019]
    assert "The Hollow Deep" in result[2022]
    assert "Glass Meridian" in result[2018]
    assert "Ember and Ash" in result[2017]


