# About
Pre-assignment for Vincit 2020 summer internship. The goal was to create a "button pressing game" web app. Done with a Python Flask back-end and React front-end.

The game is available for a limited time on [Heroku](http://kimsappi-vincit2020.herokuapp.com/). The deployment is limited in that scores and accounts will be reset after 30 minutes of inactivity.

# Instructions
## Installation
Requires Python 3 and npm (e.g. `sudo apt-get install python3 npm`) and Python module Flask (e.g. `pip3 install flask`).
```shell
git clone https://github.com/kimsappi/vincit2020.git
cd vincit2020/frontend/
npm install
npm run build
cd ../backend/
python3 app.py
```
There's also a Dockerfile available, should that be your preference.
## Usage
Point your browser to the app (default <0.0.0.0:5000>).

# Potential improvements
* proper database for managing scores
* more robust authentication (+require username and/or password)
* error handling
* more mobile-friendly design
* actual web server
* etc.