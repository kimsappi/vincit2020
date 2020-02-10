import React from 'react';

class GameDisplay extends React.Component {
	render() {
		return (
			<>
				<div id="username">
					{window.username}
				</div>
				<div id="points">
					{window.userPoints}
				</div>
				<div>
					<input type="button" id="click" value="Click me" />
				</div>
				<div id="points_to_win">
					{window.pointsToWin}
				</div>
			</>
		);
	}
}

export default GameDisplay;