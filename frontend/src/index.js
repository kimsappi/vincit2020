import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import LoginForm from './LoginForm';
import submitLogin from './loginFunctions.js';

/*
** Initialise page with login form
*/
ReactDOM.render(<LoginForm />, document.getElementById('root'));
document.getElementById("login").addEventListener("click", submitLogin);