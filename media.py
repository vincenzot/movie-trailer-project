class Movie():

    """
    Attribute description
    -------------------------
    title:
        It's the movie title

    picture:
        It's the film image url
        ex. "http://nsa37.casimages.com/img/2015/09/25/150925121855869372.jpg"

    
    
    """
    def __init__(self,
                 title,
                 picture,
                 year,
                 lenght,
                 trailer_url,
                 director,
                 genre,
                 actors,
                 plot,
                 mpaa_icon):
        
        self.title = title
        self.poster_image_url = picture
        self.year = year
        self.lenght = lenght
        self.trailer_url = trailer_url
        self.director = director
        self.genre = genre
        self.actors = actors
        self.plot = plot
        self.mpaa_icon = mpaa_icon
