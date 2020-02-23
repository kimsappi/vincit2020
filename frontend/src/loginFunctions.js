import React from 'react';
import ReactDOM from 'react-dom';
import displayGame from './game';
import LoginForm from './LoginForm';

/*
** Proceed to game or or inform user about failed login depending on response
*/
function loginResponse(data) {
	if (!data) {
		ReactDOM.render(
			<>
				<p>Invalid username or password</p>
				<LoginForm />
			</>,
			document.getElementById('root')
		);
		document.getElementById("login").addEventListener("click", submitLogin);
	}
	else {
		displayGame(data);
	}
}

/*
** Submit login details for user identification
*/
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
	.then((data) => { loginResponse(data); });
}

export default submitLogin;