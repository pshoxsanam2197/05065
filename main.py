class Mashina:
    def __init__(self, rang):
        self.__rang = rang

    def get_rang(self):
        return self.__rang

    def set_rang(self, rang):
        self.__rang = rang

m = Mashina("Qora")
print(m.get_rang())

m.set_rang("Oq")
print(m.get_rang())
