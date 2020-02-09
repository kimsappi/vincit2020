import hashlib

from flask import Flask, jsonify, request, render_template

import utils
from User import User

""" Configuration data """
cfg_salt = "m4ximal$3cur1ty"
cfg_initial_points = 20
cfg_victory_breakpoints =	{
								10: 	5,
								100: 	40,
								500: 	250
							}	
"""
About cfg_victory_breakpoints:
Key: Clicks required to win.
Value: Points given for victory.
Must be in ascending order by key.
If other breakpoints aren't multiples of first breakpoint, fix '#BREAKPOINTLOGIC'.
Value shouldn't be 0 (winning 0 points wouldn't be very fun anyway).
"""


app = Flask(__name__)
g_users = {} # Could use a DB to store users and points, but this will do for now
			# Dict because gotta go fast #PrematureOptimisation #WrongLanguage
g_counter = 0 # Could use a DB


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/login", methods=["POST"])
def begin_game():
	user = utils.identify_user(request.form)
	if user:
		return jsonify(user_points=user.points,
						points_to_win=utils.get_points_to_next_win()
						)
	else:
		return jsonify(False)


@app.route("/click", methods=["POST"])
def click():
	user = utils.identify_user(request.form)
	if user:
		user.click()
		victory_points = check_victory()
		if victory_points:
			user.add_victory(victory_points)
		return jsonify(user_points=user.points,
						victory_points=victory_points,
						points_to_win=utils.get_points_to_next_win())
	else:
		return jsonify(False)


if __name__ == "__main__":
	app.run(host="0.0.0.0")