import os

class UserManager:
	def __init__(self) -> None:
		self.users = {}

	def load_users(self):
			file_path = os.path.join('utils/data', 'Accounts.txt')
			users = []
			if os.path.exists(file_path):
				with open(file_path, 'r') as file:
					lines = file.readlines()
					for line in lines:
						parts = line.strip().split(',')
						username = parts[0]
						password = parts[1]
						users.append((username, password))
			return users

	def save_user(self, username, password):
		user_folder = 'utils/data'    
		user_file_path = os.path.join(user_folder, 'Accounts.txt')

		if not os.path.exists(user_folder):
			os.makedirs(user_folder)

		with open(user_file_path, 'a+') as file:
			file.write(f"{username},{password}\n")

	def validate_account(self, username, password):
		account_list = 	self.load_users()
		if (username, password) in account_list:
					print("Username already exists")
					return
		else:
			self.save_user(username, password)

	def register(self):
		print("Registration")
		while True:
			username = input("Enter username(at least 4 characters), leave blank to cancel: ")
			if len(username) < 4:
				print("Username must be 4 characters long")
				continue
			password = input("Enter password(at least 8 characters), leave blank to cancel: ")
			if len(password) < 8 :
				print("Password must be 8 characters long")
				continue
			if username == "" or password == "":
				continue
			self.validate_account(username, password)
			print("Registration Successful!")
			return
			
	def login(self, username, password):
		account_list = 	self.load_users()
		while True:
			if (username, password) in account_list:
				print("Log in Successful")
				return
			else:
				print("Invalid Username or Password")
				return
