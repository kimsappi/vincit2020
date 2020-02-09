class Login_Form extends React.Component() {
	render() {
		return React.createElement(
			"form",
			{ action: "login", method: "POST" },
			React.createElement(
				"label",
				{ "for": "username" },
				"Username"
			),
			React.createElement("input", { type: "text", name: "username", id: "username" }),
			React.createElement(
				"label",
				{ "for": "password" },
				"Other"
			),
			React.createElement("input", { type: "password", name: "password", id: "password" }),
			React.createElement("input", { type: "submit", value: "Submit" })
		);
	}
}

function render_login() {
	ReactDOM.render(React.createElement(Login_Form, null), document.getElementById("content"));
}
