import React from 'react';

function LoginForm() {
	return (
		<form action="login" method="POST">
			<div>
				<label for="username">Username </label>
				<input type="text" name="username" id="username" />
			</div>
			<div>
				<label for="password">Password </label>
				<input type="password" name="password" id="password" />
			</div>
			<div>
				<input type="submit" value="Submit" />
			</div>
		</form>
	);
}

export default LoginForm;