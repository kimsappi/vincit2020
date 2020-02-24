import React from 'react';

/*
** The main game display
*/
class GameDisplay extends React.Component {
	render() {
		return (
			<>
				<div>Current points</div>
				<div id="points" class="point_value">
					{window.userPoints}
				</div>
				<div id="victory_points" class="point_value">
					&nbsp;
				</div>
				<div>
					<input type="button" id="click" value="Click Me!" />
				</div>
				<div>Clicks to next prize
					<sup class="tooltip">
						?
						<div class="tooltip_text">Global counter for all players</div>
					</sup>
				</div>
				<div id="points_to_win" class="point_value">
					{window.pointsToWin}
				</div>
			</>
		);
	}
}

export default GameDisplay;