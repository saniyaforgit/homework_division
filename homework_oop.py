# -----Задание 1. Timer-----

# class Timer:
#     def __init__(self):
#         self.seconds = 0

#     def add(self, value):
#         self.seconds += value

#     def reset(self):
#         self.seconds = 0

#     def get_time(self):
#         minutes = self.seconds // 60
#         seconds = self.seconds % 60
#         return f"{minutes:02d}:{seconds:02d}"


# # пример использования
# timer = Timer()
# timer.add(65)
# print(timer.get_time())  # 01:05

# -------Задание 2. Playlist--------

# class Playlist:
#     def __init__(self):
#         self.songs = []

#     def add_song(self, title):
#         self.songs.append(title)

#     def remove_song(self, title):
#         if title in self.songs:
#             self.songs.remove(title)

#     def count(self):
#         return len(self.songs)

#     def show(self):
#         for song in self.songs:
#             print(song)


# # пример использования
# playlist = Playlist()
# playlist.add_song("Imagine")
# playlist.add_song("Yesterday")
# playlist.add_song("Hey Jude")

# playlist.show()
# print("Количество песен:", playlist.count())

# playlist.remove_song("Yesterday")
# playlist.show()

# ------Задание 4. SafeBankAccount-------

class SafeBankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Ошибка")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Ошибка")

    def get_balance(self):
        return self.balance
