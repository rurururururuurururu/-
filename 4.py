
class Film:
    def __init__(self, title, reshisser, god_vypuska):
        self.title = title
        self.reshisser = reshisser
        self.god_vypuska = god_vypuska
    def film(self):
        print(f"Фильм: {self.title}, Режиссер: {self.reshisser}, Год выпуска: {self.god_vypuska}")


movie = Film("Зеленый слоник", "Светлана Баскова", 1999)
movie.film()