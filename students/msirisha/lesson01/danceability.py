#
# This script takes care of retrieving get artists and song names for tracks with danceability scores
# over 0.8 and loudness scores below -5.0. In other words, quiet yet danceable tracks.
# Also, these tracks should be sorted in descending order by danceability so that the most
# danceable tracks are up top. You should be able to work your way there starting with the comprehension above.
#
import pandas

music = pandas.read_csv("featuresdf.csv")


def get_song_names_and_artists():
    """
    This method prints the artist name and track names with quiet danceable tracks. That means with danceability > 0.8
    and loudness < -5.0
    :return:  Returns list of tuples. The tuple contains artist name and track name.
    """
    return [(a, n, d, l) for a, n, d, l in sorted(zip(music.artists, music.name, music.danceability, music.loudness),
                                                  key=lambda x: x[2], reverse=True) if d > 0.8 and l < -5.0]


def get_top_five_track_names():
    """
    This method calls the above get song names and artists names method and returns top five danceable tracks.
    :return: Returns top five danceable track names.
    """
    return [artist_song_tuple[1] for artist_song_tuple in get_song_names_and_artists()[:5]]


print("Artist and track names with danceability > 0.8 and loudness < -5.0")
print(get_song_names_and_artists())
print("\nTop five track names")
print(get_top_five_track_names())
