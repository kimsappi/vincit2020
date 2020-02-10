import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import LoginForm from './LoginForm';
import * as serviceWorker from './serviceWorker';
import submitLogin from './functions.js';

ReactDOM.render(<LoginForm />, document.getElementById('root'));
document.getElementById("login").addEventListener("click", submitLogin);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
