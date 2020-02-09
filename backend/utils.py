from User import User

def check_victory() -> int:
	""" Returns number of points won (no victory -> 0) """
	points = 0
	for breakpoint in iter(cfg_victory_breakpoints.items()):
		if g_counter % breakpoint[0] == 0:
			if breakpoint[1] > points:
				points = breakpoint[1]
	return points


def get_points_to_next_win() -> int:
	""" Returns number of points required for next victory """
	#BREAKPOINTLOGIC
	victory_interval = next(iter(cfg_victory_breakpoints.keys()))
	points_to_win = victory_interval - (g_counter % victory_interval)


def hash_password(username: str, password: str) -> str:
	""" Returns salted password hash for given username and password """
	return hashlib.md5(str(hash(username + cfg_salt)))


def identify_user(data: dict) -> User:
	"""
	Returns user objects (creates if necessary) that matches user data or None
	if submitted data is incorrect or incomplete
	"""
	#try:
	username = data.get("username")
	password = data.get("password")
	user = g_users.get(username)
	if user: # We already have data for the user
		if not user.validate_password(password):
			return None
	else: # Create new user
		user = User(username=username, password=password)
	return user
	#except:
		#return None