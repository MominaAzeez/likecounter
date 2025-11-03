from LikeCounter import UpCounter, DownCounter, LikeList, User, Button

def main():
       print("=== Counter Demo ===")
    up = UpCounter(start=0, step=2)
    down = DownCounter(start=10, step=3)

    print("UpCounter advancing:")
    for _ in range(3):
        print(up.advance())

    print("\nDownCounter advancing:")
    for _ in range(3):
        print(down.advance())

     print("\n=== LikeList Demo ===")
    likes = LikeList()
    u1 = User("Maryam")
    u2 = User("Amara")

    likes.add_user(u1)
    likes.add_user(u2)
    likes.show_likes()

    likes.remove_user(u1)
    likes.show_likes()

       print("\n=== Button Demo ===")
    btn = Button()
    btn.draw()
    btn.click()


if __name__ == "__main__":
    main()
