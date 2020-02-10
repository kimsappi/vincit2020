import React from 'react';

function LoginForm() {
	return (
		<>
			<div>
				<label for="username">Username</label>
				<input type="text" name="username" id="login_username" />
			</div>
			<div>
				<label for="password">Password</label>
				<input type="password" name="password" id="login_password" />
			</div>
			<div>
				<input type="submit" value="Submit" id="login" />
			</div>
		</>
	);
}

export default LoginForm;