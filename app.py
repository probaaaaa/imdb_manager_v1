import install_requirements
import random
import csv
from selenium import webdriver
from functions import *

# =================================
# CHOOSE A RANDOM MOVIE
# =================================
with open('WATCHLIST.csv') as f:
    rows = csv.DictReader(f, delimiter=',', quotechar='"')
    movies = [row for row in rows if row['Title Type'] == 'movie']

movie = random.choice(movies)
text = """There are {num} feature films in your watchlist.

I have chosen the following movie for you:

===========================================

    \x1b[1m{Title}\x1b[0m ({Year})

    IMDb Rating:    {IMDb Rating}
    Genres:         {Genres}
    Runtime:        {Runtime (mins)}min
    Link:           {URL}

===========================================

You have two options:
1 - Rate "{Title}" (also removes it from the watchlist)
2 - Remove "{Title}" from your watchlist
"""
print(text.format(num=len(movies), **movie))


def main():
    choice = int(input('Choose an option: '))
    while True:
        options = webdriver.ChromeOptions()
        # options.headless = True
        driver = webdriver.Chrome(options=options)
        if choice == 1:
            print('You chose to rate "{Title}".'.format(**movie))
            locate_movie(driver, movie)
            rate_movie(driver, movie)
            print('Goodbye.')
            break
        elif choice == 2:
            print('You chose to remove "{Title}" from your watchlist.'.format(**movie))
            locate_movie(driver, movie)
            remove_movie(driver, movie)
            print('Goodbye.')
            break


if __name__ == '__main__':
    main()
