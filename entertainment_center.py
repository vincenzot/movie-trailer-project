import fresh_tomatoes
import media

TITANIC = media.Movie("Titanic",
                      "http://nsa37.casimages.com/img/2015/09/25/150925121855869372.jpg",
                      "1997",
                      "194",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ",
                      "James Cameron",
                      "Drama, Romance",
                      "Leonardo DiCaprio, Kate Winslet, Billy Zane",
                      "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                      "16 January 1998",
                      "PG-13",
                      "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/RATED_PG-13.svg/2000px-RATED_PG-13.svg.png")

BENVENUTI_AL_SUD = media.Movie("Benvenuti al Sud",
                      "https://upload.wikimedia.org/wikipedia/en/2/21/Benvenuti_al_Sud.jpg",
                      "2010",
                      "106",
                      "https://www.youtube.com/watch?v=3JtQfHPPGS8",
                      "Luca Miniero",
                      "Comedy",
                      "Claudio Bisio, Alessandro Siani, Angela Finocchiaro",
                      "Overwhelmed by his wife, a Northern Italy postal worker feigns a disability to request a transfer to Milan and when he's unmasked is sent for two years to a far and tiny village near Naples",
                      "1 October 2010",
                      "G",
                      "https://upload.wikimedia.org/wikipedia/commons/0/05/RATED_G.svg")

THE_SOCIAL_NETWORK = media.Movie("The Social Network",
                      "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                      "2010",
                      "120",
                      "https://www.youtube.com/watch?v=3JtQfHPPGS8",
                      "Luca Miniero",
                      "Comedy, Biographic, Dramatic",
                      "Claudio Bisio, Alessandro Siani, Angela Finocchiaro",
                      "Overwhelmed by his wife, a Northern Italy postal worker feigns a disability to request a transfer to Milan and when he's unmasked is sent for two years to a far and tiny village near Naples",
                      "1 October 2010",
                      "PG-13",
                      "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/RATED_PG-13.svg/2000px-RATED_PG-13.svg.png")


movies = [TITANIC,
          BENVENUTI_AL_SUD,
          THE_SOCIAL_NETWORK]

fresh_tomatoes.open_movies_page(movies)
