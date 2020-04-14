Questions and Answers Framework
A simple question and answers framework.

Live Version: https://qandaproduction.herokuapp.com/

We are open to contributions. Send a pull request if you feel you can fix some bugs.

Requirements:
Python 3+
Djanog 2.0+

Installation:
1) git clone https://www.github.com/satyamfouzdar/quanda-local/
2) python3 -m venv venv (for windows python -m venv venv)
3) source venv/bin/activate (for windows venv/Scripts/activate)
4) cd quanda-local
5) pip install -r requirements.txt
6) ./manage.py migrate
7) ./manage.py runserver

Note: The app uses sqlite by default but if you want to use you own postgresql database, just pass the database_url in the DATABASE_URL environment variable. (export DATABASE_URL=<databaseurl>)
