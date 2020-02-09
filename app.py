from hashlib import md5

from flask import Flask, jsonify, request, render_template

""" Configuration data """
cfg_salt = "m4ximal$3cur1ty"
cfg_initial_points = 20
cfg_victory_breakpoints =	{
								10: 	5,	# Key: Clicks required to win
								100: 	40,	# Value: Points given for victory
								500: 	250	# Must be in ascending order by key
							}	# If other breakpoints aren't multiples of first
								# breakpoint, fix '#BREAKPOINTLOGIC'


app = Flask(__name__)
g_users = {} # Could use a DB to store users and points, but this will do for now
			# Dict because gotta go fast #PrematureOptimisation #WrongLanguage
g_counter = 0 # Could use a DB


class User():
	def __init__(self, username: str, password: str) -> None:
		self.username = username
		self.password = hash_password(username, password)
		self.points = cfg_initial_points
		g_users[username] = self

	def click(self) -> bool:
		if self.points > 0:
			self.points -= 1
			return True
		else:
			return False
	
	def reset_points(self) -> bool:
		if self.points < 1:
			self.points = cfg_initial_points
			return True
		else:
			return False

	def validate_password(self, password) -> bool:
		return password == hash_password(self.username, password)

	def victory(self, points: int) -> None:
		self.points += points


def hash_password(username: str, password: str) -> str:
	return md5(str(hash(username + cfg_salt)))


def get_points_to_next_win() -> int:
	""" Returns number of points required for next victory """
	#BREAKPOINTLOGIC
	victory_interval = next(iter(cfg_victory_breakpoints.keys()))
	points_to_win = victory_interval - (g_counter % victory_interval)


def get_user_points(ip: str) -> int:
	initial_points = points.get(ip)
	if not initial_points:
		points[ip] = cfg_initial_points
		initial_points = cfg_initial_points


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/login", methods=["POST"])
def begin_game():
	username = request.form.get("username")
	password = request.form.get("password")
	user = g_users.get(username)
	if user and not user.validate_password(password):
		return jsonify(False)
	else:
		user = User(username=username, password=password)
	return jsonify(user_points=user.points,
					points_to_win=get_points_to_next_win()
					)


@app.route("/click", methods=["POST"])
def click():
	pass


if __name__ == "__main__":
	app.run(host="0.0.0.0")