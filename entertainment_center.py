import fresh_tomatoes
import media


# Create Movie instances containing movie title, poster image url, and trailer youtube url
big_hero_6 = media.Movie("Big Hero 6",
                         "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=z3biFxZIJOQ")

flyboys = media.Movie("Flyboys",
                      "https://upload.wikimedia.org/wikipedia/en/8/85/Flyboys_Final1Sheet2.jpg",
                      "https://www.youtube.com/watch?v=fpIXMVSnsOY")

forrest_gump = media.Movie("Forrest Gump",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")

pacific_rim = media.Movie("Pacific Rim",
                          "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",
                          "https://www.youtube.com/watch?v=5guMumPFBag")

thor = media.Movie("Thor",
                   "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

titanic = media.Movie("Titanic",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

# Store Movie instances in a list of favorite movies
favorite_movies_list = [big_hero_6, flyboys, forrest_gump, pacific_rim, thor, titanic]

# Build a static webpage containing the list of favorite movies
fresh_tomatoes.open_movies_page(favorite_movies_list)
