import webbrowser


""" Class for showing a movie """
class Movie():

    """
        Initalize a Movie object
        Attributes:
            title: A string of the movie's title
            poster_url: A string of the URL to the movie's poster image
            trailer_youtube_url: A string of theURL to the movie's youtube trailer
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    """ Opens trailer in a web browser """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
