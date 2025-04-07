class Movies:
    def __init__(self):
        self.movies = []

    def add_mives(self, movie):
        self.movies.append(movie)


# напиши свой код здесь
class Comedy(Movies):

    def add_mives(self, movie):
        self.movies.append(movie)
        return f"Комедия: {self.movies}"


class Drama(Movies):

    def add_mives(self, movie):
        self.movies.append(movie)
        return f"Драма: {self.movies}"


comedy = Comedy()
print(comedy.add_mives("Оружейный барон"))

drama = Drama()
print(drama.add_mives("Оружейный барон"))
