import React from 'react';
import ReactDOM from 'react-dom';
import GameDisplay from './GameDisplay';

function displayGame(data) {
	window.user_points = data.user_points;
	window.points_to_win = data.points_to_win;
	ReactDOM.render(
		<GameDisplay />,
		document.getElementById('root')
	);
}

export default displayGame;