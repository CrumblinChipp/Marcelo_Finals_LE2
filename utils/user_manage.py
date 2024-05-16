import os

class UserManager:
	user_dict = {}
    
	def user_dict(self):
		with open("data/Accounts.txt", 'r') as file:
			for line in file:
				username, password = line.strip().split(', ')
				self.user_dict[username] = password
		file.close()
  
	def load_users():
		if not os.path.exists("data"):
			os.makedirs("data")

	def save_users(self, user, key):
		self.load_users()
		f = open("data/Accounts.txt", "a")
		f.write(f"{user},{key}")
		f.close()
		pass

	def validate_username(self, username):
		self.user_dict()
		if username in self.user_dict.key():
			return False
		else:
			return True

	def validate_password(self, username, password):
		self.user_dict()
		if password == self.user_dict[username]:
			return False
		else:
			return True

	def register(self):
		print("Registration")
		file_path = "data/Accounts.txt"
		while True:
			username = input("Enter username(at least 4 characters), leave blank to cancel: ")
			if len(username) < 4:
				print("username must be 4 characters long")
				continue
			if self.validate_username(username) == False:
				print("Username is already used")
				continue
			password = input("Enter password(at least 8 characters), leave blank to cancel: ")
			if len(username) < 8:
				print("Password must be 4 characters long")
				continue
			if self.validate_password(username, password) == False:
				print("Username is already used")
				continue
			if username == "" or password == "":
				break
			self.save_users(username, password)
			print("Registration Successful!")

user = UserManager()
user.register()