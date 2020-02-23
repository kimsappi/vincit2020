import hashlib
import json
from typing import List

import config
from User import User

def check_victory(counter: int) -> int:
	""" Returns number of points won (no victory -> 0) """
	points = 0
	for breakpoint in iter(config.victory_breakpoints.items()):
		if counter % breakpoint[0] == 0:
			if breakpoint[1] > points:
				points = breakpoint[1]
	return points


def get_leaderboard(users: List[dict]):
	if not len(users): # No users yet, display something else
		return jsonify(False)
	user_list = list(users.values())
	user_list.sort(reverse=True)
	user_list_dicts = [user.public_data_to_dict() for user in user_list]
	return user_list_dicts


def get_points_to_next_win(counter: int) -> int:
	""" Returns number of points required for next victory """
	#BREAKPOINTLOGIC
	victory_interval = next(iter(config.victory_breakpoints.keys()))
	points_to_win = victory_interval - (counter % victory_interval)
	return points_to_win


def hash_password(username: str, password: str) -> str:
	""" Returns salted password hash for given username and password """
	salt = hashlib.md5((username + config.salt).encode("utf-8")).hexdigest()
	return hashlib.sha256((password + salt).encode("utf-8")).hexdigest()


def identify_user(data: dict, users: dict) -> User:
	"""
	Returns user objects (creates if necessary) that matches user data or None
	if submitted data is incorrect or incomplete
	"""
	try:
		data = json.loads(data.decode("utf-8"))
		username = data.get("username")
		password = data.get("password")
		user = users.get(username)
		if user: # We already have data for the username
			if not user.validate_password(password):
				return None
		else: # Create new user
			user = User(username=username, password=password, users=users)
		return user
	except:
		return None