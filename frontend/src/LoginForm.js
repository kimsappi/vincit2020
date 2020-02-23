import React from 'react';

function LoginForm() {
	return (
		<>
			<h1>Log in</h1>
			<p>You can register by entering an unused username and password.</p>
			<div>
				<div><label for="username">Username</label></div>
				<input type="text" name="username" id="login_username" />
			</div>
			<div>
				<div><label for="password">Password</label></div>
				<input type="password" name="password" id="login_password" />
			</div>
			<div>
				<input type="submit" value="Submit" id="login" />
			</div>
		</>
	);
}

export default LoginForm;