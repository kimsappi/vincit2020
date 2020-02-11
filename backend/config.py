""" Configuration data """
salt = "m4ximal$3cur1ty" # Extra password security
initial_points = 20 # Number of points given to starting players
victory_breakpoints =	{
							10: 	5,
							100: 	40,
							500: 	250
						}	
"""
About victory_breakpoints:
Key: Clicks required to win.
Value: Points given for victory.
Must be in ascending order by key.
If other breakpoints aren't multiples of first breakpoint, fix '#BREAKPOINTLOGIC'.
Value shouldn't be 0 (winning 0 points wouldn't be very fun anyway).
"""