from utils import dice_game, user_manage

def main():
    user = user_manage.UserManager()
    print("Welcome to Dice Roll Game!")
    print("1. Register")
    print("2. Log in")
    print("3. Exit")
    while True:
        try:
            action = int(input("enter choice, or leave blank to return: "))
        except Exception:
            print("Please only enter 1-3")
            continue
        if action == 1:
            user.register()
        elif action == 2:
            user.login()
        elif action == 3:
            exit()
        else:
            print("Invalid Input.Please only enter 1-3")
    
    
if __name__ == "__main__":
    main()