import React from 'react';
import ReactDOM from 'react-dom';
import GameDisplay from './GameDisplay';

function clickResetPoints() {
	const loginData = {
		username: window.username,
		password: window.password
	}
	fetch("/reset", {
		method: "post",
		headers: new Headers({'content-type': 'application/json'}),
		body: JSON.stringify(loginData)
	})
	.then((response) => { return response.json(); })
	.then((data) => {
		window.userPoints = data.user_points;
		window.pointsToWin = data.points_to_win;
		renderGame();
	});
}

function clickResponse(response) {
	window.userPoints = response.user_points;
	window.pointsToWin = response.points_to_win;
	renderGame();

	// User ran out of points, ask if they want to restart
	if (!response.user_points &&
		window.confirm("Unfortunately you seem to have 0 points. Restart at 20 points?")) {
		clickResetPoints();
	}
}

function clickUpdatePoints() {
	if (window.userPoints) {
		window.userPoints -= 1;
	}
}

function clickButton() {
	const loginData = {
		username: window.username,
		password: window.password
	}
	clickUpdatePoints();

	fetch("/click", {
		method: "post",
		headers: new Headers({'content-type': 'application/json'}),
		body: JSON.stringify(loginData)
	})
	.then((response) => { return response.json(); })
	.then((data) => { clickResponse(data); });
}

function displayGame(data) {
	window.userPoints = data.user_points;
	window.pointsToWin = data.points_to_win;
	renderGame();
	document.getElementById("click").addEventListener("click", clickButton);
}

function renderGame() {
	ReactDOM.render(
		<GameDisplay />,
		document.getElementById("root")
	);
}


export default displayGame;