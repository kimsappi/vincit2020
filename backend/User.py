import config
import utils

class User():
	def __init__(self, username: str, password: str, users: dict) -> None:
		self.username = username
		self.password = utils.hash_password(username, password)
		self.points = config.initial_points
		self.resets = 0
		self.victories = {points: 0 for points in iter(config.victory_breakpoints.values())}

		users[username] = self # Add to global user dict

	def __lt__(self, other) -> bool: # Sort users by points
		return self.points < other.points

	def add_victory(self, points: int) -> None:
		self.points += points
		self.victories[points] += 1

	def click(self) -> bool:
		if self.points > 0:
			self.points -= 1
			return True
		else:
			return False

	def public_data_to_dict(self) -> dict:
		return {
			"username": self.username,
			"points": self.points,
			"resets": self.resets,
			"victories": self.victories
		}
	
	def reset_points(self) -> bool:
		if self.points < 1:
			self.points = config.initial_points
			return True
		else:
			return False

	def validate_password(self, password: str) -> bool:
		return self.password == utils.hash_password(self.username, password)

	def victory(self, points: int) -> None:
		self.points += points