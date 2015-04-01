Last login: Mon Feb  9 14:11:42 on ttys001

guest-2-00926:j583-assignments currine$ mkvirtualenv djangogirls --python=`which python`
Running virtualenv with interpreter /usr/local/bin/python
New python executable in djangogirls/bin/python2.7
Also creating executable in djangogirls/bin/python
Installing setuptools, pip...done.

(djangogirls)guest-2-00926:j583-assignments currine$ pip install Django==1.7
You are using pip version 6.0.7, however version 6.0.8 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
Collecting Django==1.7
  Downloading Django-1.7-py2.py3-none-any.whl (7.4MB)
    100% |################################| 7.4MB 55kB/s 
Installing collected packages: Django

Successfully installed Django-1.7

(djangogirls)guest-2-00926:j583-assignments currine$ ls
IntroDjango	README.md	assignment4.py	assignment5.py	newschool

(djangogirls)guest-2-00926:j583-assignments currine$ django-admin.py startproject djangogirls

(djangogirls)guest-2-00926:j583-assignments currine$ cd djangogirls/

(djangogirls)guest-2-00926:djangogirls currine$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, contenttypes, auth, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK

(djangogirls)guest-2-00926:djangogirls currine$ python manage.py runserver
Performing system checks...
System check identified no issues (0 silenced).
February 10, 2015 - 00:08:11
Django version 1.7, using settings 'djangogirls.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[10/Feb/2015 00:08:20] "GET / HTTP/1.1" 200 1759
[10/Feb/2015 00:08:20] "GET /favicon.ico HTTP/1.1" 404 1932