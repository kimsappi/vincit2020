import React from 'react';

function GameDisplay(data) {
	return (
		<>
			<div id="username">
				{window.username}
			</div>
			<div id="points">
				{window.user_points}
			</div>
			<div>
				<input type="button" id="click" value="Click me" />
			</div>
			<div id="points_to_win">
				{window.points_to_win}
			</div>
		</>
	);
}

export default GameDisplay;