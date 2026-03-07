from IteratorCollection import MovieCollection
def stream_netflix():
    top_movies = MovieCollection()
    favorite_movies = MovieCollection()

    top_movies.add_movie('Die Hard')
    top_movies.add_movie('Inception')
    top_movies.add_movie('Oppenheimer')

    favorite_movies.add_movie('La la Land')
    favorite_movies.add_movie('Jerry Maguire')

    top_movie_iter = top_movies.create_iterator()

    while top_movie_iter.has_next():
        print(f'Streaming top movie: {top_movie_iter.next()}')

    print()
    fav_movie_iter = favorite_movies.create_iterator()
    while fav_movie_iter.has_next():
        print(f'Streaming favorite movie: {fav_movie_iter.next()}')


if __name__=='__main__':
    stream_netflix()
