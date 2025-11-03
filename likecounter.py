from abc import ABC, abstractmethod

class Counter(ABC):
    def __init__(self, start=0):
        self.current = start

    @abstractmethod
    def advance(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.advance()
        return self.current


class UpDownCounter(Counter):
    @abstractmethod
    def advance(self):
        pass



class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class LikeList:
    def __init__(self):
        self.users = []  # composition: LikeList owns Users

    def add_user(self, user: User):
        self.users.append(user)

    def remove_user(self, user: User):
        if user in self.users:
            self.users.remove(user)

    def show_likes(self):
        print("Liked by:", ", ".join(str(u) for u in self.users) or "No one yet")


class Polygon:
    def draw(self):
        print("Drawing a polygon...")
