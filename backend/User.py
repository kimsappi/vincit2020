class User():
	def __init__(self, username: str, password: str) -> None:
		self.username = username
		self.password = hash_password(username, password)
		self.points = cfg_initial_points
		self.resets = 0
		self.victories = {points: 0 for points in iter(cfg_victory_breakpoints.values())}

		g_users[username] = self

	def add_victory(self, points: int) -> None:
		self.points += points
		self.victories[points] += 1

	def click(self) -> bool:
		if self.points > 0:
			self.points -= 1
			g_counter += 1
			return True
		else:
			return False
	
	def reset_points(self) -> bool:
		if self.points < 1:
			self.points = cfg_initial_points
			return True
		else:
			return False

	def validate_password(self, password: str) -> bool:
		return password == utils.hash_password(self.username, password)

	def victory(self, points: int) -> None:
		self.points += points