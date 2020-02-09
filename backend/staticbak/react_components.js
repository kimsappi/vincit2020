class Login_Form extends React.Component() {
	render() {
		return(
			<form action="login" method="POST">
				<label for="username">Username</label>
				<input type="text" name="username" id="username" />
				<label for="password">Other</label>
				<input type="password" name="password" id="password" />
				<input type="submit" value="Submit" />
			</form>
		)
	}
}