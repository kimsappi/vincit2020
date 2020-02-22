from flask import Flask, jsonify, request, render_template

import config
import utils
from User import User

app = Flask(__name__)
g_users = {} # Could use a DB to store users and points, but this will do for now
			# Dict is fast
g_counter = 0 # Could use a DB


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/login", methods=["POST"])
def begin_game():
	user = utils.identify_user(request.get_data(), g_users)
	if user:
		points_to_win = utils.get_points_to_next_win(g_counter)
		return jsonify	(
							user_points=user.points,
							leaderboard=utils.get_leaderboard(g_users)
						)
	else:
		return jsonify(False)


@app.route("/click", methods=["POST"])
def click():
	global g_counter

	user = utils.identify_user(request.get_data(), g_users)
	if user:
		click_success = user.click()
		if click_success: # User had points, click successful
			g_counter += 1
			victory_points = utils.check_victory(g_counter)
		else: # No points left
			victory_points = 0
		if victory_points:
			user.add_victory(victory_points)

		if user.points:
			points_to_win = utils.get_points_to_next_win(g_counter)
		else:
			points_to_win = '?' # Hiding game state from 0-point users
		return jsonify	(
							user_points=user.points,
							victory_points=victory_points,
							points_to_win=points_to_win,
							leaderboard=utils.get_leaderboard(g_users)
						)
	else:
		return jsonify(False)


@app.route("/reset", methods=["POST"])
def reset_points():
	user = utils.identify_user(request.get_data(), g_users)
	if user:
		user.reset_points()
		return jsonify	(
							user_points=user.points,
							leaderboard=utils.get_leaderboard(g_users)
						)
	else:
		return jsonify(False)


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)