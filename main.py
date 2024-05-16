from utils import dice_game, user_manage

def main():
    user = user_manage.UserManager()
    dice = dice_game.DiceGame()
    while True:
        print("============================")
        print("Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Log in")
        print("3. Exit")
        try:
            action = int(input("enter choice, or leave blank to return: "))
        except Exception:
            print("Please only enter 1-3")
            continue
        if action == 1:
            user.register()
        elif action == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user.login(username, password)
            dice.menu(username)
        elif action == 3:
            exit()
        else:
            print("Invalid Input.Please only enter 1-3")


if __name__ == "__main__":
    main()