import React from 'react';
import ReactDOM from 'react-dom';
import displayGame from './game';

function loginResponse(data) {
	if (!data) {
		ReactDOM.render(
			<div>Invalid username or password</div>,
			document.getElementById('root')
		);
	}
	else {
		displayGame(data);
	}
}

function submitLogin() {
	window.username = document.getElementById("login_username").value
	window.password = document.getElementById("login_password").value
	const loginData = {
		username: window.username,
		password: window.password
	}
	
	fetch("/login", {
		method: "post",
		headers: new Headers({'content-type': 'application/json'}),
		body: JSON.stringify(loginData)
	})
	.then((response) => { return response.json(); })
	.then((data) => {console.log(data); loginResponse(data); });
}

export default submitLogin;