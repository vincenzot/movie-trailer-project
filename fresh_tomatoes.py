import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<html>
<head>
    <meta charset="utf-8">
    <title>Movie Trailer List - Project 1 - Vincenzo Tartaglia</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <!-- Including jQuery Shorten Plugin -->
    <script type="text/javascript"
	src="http://viralpatel.net/blogs/demo/jquery/jquery.shorten.1.0.js"></script>

    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>

<script type="text/javascript">
	$(document).ready(function() {
	
		$(".gdesc").shorten({
	"showChars" : 70,
	"moreText"	: "See More",
	"lessText"	: "Less",
});

                $(".starred").shorten({
	"showChars" : 20,
	"moreText"	: "See More",
	"lessText"	: "Less",
});
	
	});
</script>
    
    <script type="text/javascript" charset="utf-8">


        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {



            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Trailer Project</a>
          </div>
<button type="button" style="margin-top:9px;float:right;margin-left:5px;" class="btn btn-info btn-md" data-toggle="modal" data-target="#CreditsModal">Credits</button>
<button type="button" style="margin-top:9px;float:right;" class="btn btn-info btn-md" data-toggle="modal" data-target="#Mpaa">MPAA ratings</button>

        </div>


          
      </div>
    </div>

          <div class="jumbotron text-center">
              <h2>Welcome to Movie Trailer Website</h2>
              <p>Click on your favorite movie title to see the trailer</p>
          </div>

    

<!-- Modal MPAA -->
<div id="Mpaa" class="modal fade" role="dialog">
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">MPAA's Explanation</h4>
      </div>
      <div class="modal-body">

<p>MPAA is the organization that administers American film ratings.</p>      
        <table class="wikitable" style="margin: 1em auto 1em auto;">
<tbody><tr>
<th style="padding:10 20 10 10">Rating</th>
<th style="padding:10 20 10 10">Meaning</th>
<th>MPAA's Explanation</th>
</tr>
<tr>
<td align="center"><b>G</b></td>
<td>General Audiences</td>
<td>"Nothing that would offend parents for viewing by children."
<p>On the box: "All ages admitted"</p>
</td>
</tr>
<tr>
<td align="center"><b>PG</b></td>
<td>Parental Guidance Suggested</td>
<td>"Parents urged to give 'parental guidance.' May contain some material parents might not like for their young children."
<p>On the box: "Some material may not be suitable for children"</p>
</td>
</tr>
<tr>
<td align="center"><b>PG-13</b></td>
<td>Parents Strongly Cautioned</td>
<td>"Parents are urged to be cautious. Some material may be inappropriate for pre-teenagers."
<p>On the box: "Some material may be inappropriate for children under 13"</p>
</td>
</tr>
<tr>
<td align="center"><b>R</b></td>
<td>Restricted</td>
<td>"Contains some adult material. Parents are urged to learn more about the film before taking their young children with them."
<p>On the box: "Under 17 requires accompanying parent or adult guardian"</p>
</td>
</tr>
<tr>
<td align="center"><b>NC-17</b></td>
<td>Adults Only</td>
<td>"Clearly adult. Children are not admitted."
<p>On the box: "No One 17 and Under Admitted"</p>
</td>
</tr>
</tbody></table>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>

  </div>
</div>




<!-- Modal Credits-->
<div id="CreditsModal" class="modal fade" role="dialog">
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">Credits</h4>
      </div>
      <div class="modal-body">
          <p><b>Creator:</b> Vincenzo Tartaglia</p>
          <img src="http://it.seaicons.com/wp-content/uploads/2016/03/Linkedin-icon-17.png" height="40" width="40"></img><a target="_blank" href="https://it.linkedin.com/in/vincenzo-tartaglia-33474a111">View LinkedIn Profile</a>
          <br>
          <img src="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png" height="40" width="40"></img><a target="_blank" href="https://github.com/vincenzot">github.com/vincenzot</a>
          <br>
          <img src="http://cdn.sstatic.net/Sites/stackoverflow/company/img/logos/so/so-icon.png?v=c78bd457575a" height="40" width="40"></img><a target="_blank" href="http://stackoverflow.com/users/5861977/vincenzo-tartaglia">vincenzo-tartaglia</a>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>

  </div>
</div>
          
    
    <div class="container">
      {movie_tiles}
    </div>

              
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img style="position:relative; top:0; left:0; z-index:1" src="{poster_image_url}" width="220" height="342">
    <img style="position:absolute; top:20; left:310; z-index:2" src="{mpaa_icon}" width="50" height="30">
    <h2>{movie_title}<h4>({year})</h4></h2><h5><b>Director:</b> {director}</h5><h5><b>Lenght:</b> {lenght} minutes</h5><h5><b>Genre:</b> {genre}</h5><h5><b>Starred:</b> <div class="starred">{actors}</div></h5><h5><b>Plot:</b> <i><div class="gdesc">{plot}</div></i></h5>

<!-- Modal More Movie Details-->
<div id="MovieDetails" class="modal fade" role="dialog">
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">Credits</h4>
      </div>
      <div class="modal-body">

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>

  </div>
</div>

</div>




'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            lenght = movie.lenght,
            year=movie.year,
            genre=movie.genre,
            plot=movie.plot,
            actors=movie.actors,
            mpaa_icon=movie.mpaa_icon,
            director=movie.director
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
