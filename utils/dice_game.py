import random, os

class DiceGame:
	def load_scores():
		if not os.path.exists("data"):
			os.makedirs("data")

	def save_scores(self, score, stage):
		self.load_scores()
		f = open("data/ranking.txt", "a")
		f.write(f"User: Points - {score}\t, Wins - {stage}\n")
		f.close()
		pass

	def play_game(self):
		user_score = 0
		bot_score = 0
		round  = 0
		total = 0
		print("starting the game as username")
		while True:
			while user_score < 2 and bot_score < 2:
				bot_num = random.randint(1,6)
				user_num = random.randint(1,6)
				print(f"Username rolled: {user_num}")
				print(f"Bot rolled: {bot_num}")
				if user_num > bot_num:
					user_score += 1
					print("You won this round Username!")
				elif bot_num > user_num:
					bot_score += 1
					print("You lost this round Username!")	
				elif bot_num == user_num:
					print("Its a tie!")
			total += user_score
			if user_score > bot_score:
				user_score +=3
				total+= 3
				round+=1
				print("============================")
				print("You won this stage Username!")
				print(f"Total points: {total},  Stages won: {round}")
			elif user_score < bot_score:	
				print("============================")
				print("You lost the stage Username!")
				print(f"Total points: {total}\t, Stages won: {round}")
				if round >= 1:
					self.save_scores(total, round)	
				self.menu()
			if  user_score > bot_score:
				try:
					confirm = int(input("Do you want to continue to the next round? (1 for Yes, 0 for No): "))
				except Exception:
					print("Invalid Input.Enter only 1 for Yes, 0 for No")
					continue
				if confirm == 1:
					user_score = 0
					bot_score = 0
				elif confirm == 0:
					self.save_scores(total, round)
					self.menu()


	def show_top_scores(self, score, stage):
		try:
			with open("data/ranking.txt", "r") as file:
				scores = []
				for line in file.readlines():
					parts = line.split(',')
					points = int(parts[0].split('-')[1].strip())
					wins = int(parts[1].split('-')[1].strip())
					scores.append((points, wins))
					
			scores.sort(reverse=True, key=lambda x: x[0])
			
			print("Top Scores:")
			for i, (points, wins) in enumerate(scores, start=1):
				print(f"{i}. Points: {points}, Wins: {wins}")
		except FileNotFoundError:
			print("No scores yet")
		except Exception as e:
			print(f"An error occurred: {e}")
		

	def logout():
		print("Logging out...")
		exit()

	def menu(self):
		print("Welcome Username!")
		print("Menu:")
		print("1. Start Game\n2. Show top scores\n3. Log out\n")
		while True:
			try:
				action = int(input("enter choice, or leave blank to return: "))
			except Exception:
				print("Please only enter 1-3")
				continue
	
			if action == 1:
				os.system('cls')
				self.play_game()
			elif action == 2:
				if os.path.exists("data/ranking.txt") and os.stat("data/ranking.txt").st_size > 0:
					self.show_ranking()
				else:
					print("No scores yet")
			elif action == 3:
				self.logout()
			else:
				print("Invalid Input.Please only enter 1-3")
