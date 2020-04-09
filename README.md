# Movie Trailer Website
A Movie Trailer Website where users can browse featured movie list.

#Instructions
1. Download this repository;
2. Open **entertainment_center.py**;
3. If you want you can add custom movie in the list by adding this string
```
MOVIE_ID = media.Movie("Movie Title",
                      "Movie Cover URL",
                      "Publish Year",
                      "Minutes",
                      "Trailer YouTube URL",
                      "Director",
                      "Genre",
                      "Actors",
                      "Description",
                      "Mpaa icon")
```
4. Add your MOVIE_ID in the array at the bottom:
```
movies = [THE_IMITATION_GAME,
          FLASH_OF_GENIUS,
          ENIGMA,
          BENVENUTI_AL_SUD,
          THE_SOCIAL_NETWORK,
          TITANIC,
          A_BEAUTIFUL_MIND,
          BLACKJACK,
          THE_BANK,
          MOVIE_ID]
```
5. Run **entertainment_center.py**;
6. Open **fresh_tomatoes.html** file generated and use it.

# Project File Description
In this project there are these file list:
* **entertainment_center.py** - This is the script to run. It contains the movie list and calls the method from `fresh_tomatoes.py` to generate the web page.
* **fresh_tomatoes.py** - It's the web site HTML page generator. It receives the movie list from `entertainment_center.py` and uses it to generate `fresh_tomatoes.html` page. Then it will open the page with your default web browser.
* **media.py** - There is the class inside that contains the movie attributes.
* **fresh_tomatoes.html** - File generated from entertainment_center.py running.

# Live Demo
<a target="_blank" href="http://htmlpreview.github.io/?https://github.com/vincenzot/movie-trailer-website-project/blob/master/live/fresh_tomatoes.html">Click here</a> to see live demo.

# Creator

**Vincenzo Tartaglia**

  - http://github.com/vincenzot
  - https://www.linkedin.com/in/vincenzotartaglia/
  - http://stackoverflow.com/users/5861977/vincenzo-tartaglia
