# COP4710 Project
To sucessfully run this Django project you will need the following programs:
1. Install [Python 3.6.5](https://www.python.org/downloads/release/python-365/)
2. Type command on cmd.exe `pip install virtualenvwrapper-win`

    Note: This installs a virtual enviroment to install python 
    library without needing to mess up your PATH environment variable
    on windows.

3. Creating a virtual environment: `mkvirtualenv myproject`

   Note: This creates a virtual enviroment for a python project.
   the folder 'myproject' will be under a folder called Envs.

4. Initializing the virtual environment(VE): `workon myproject`
   
   Note: Initializes virtual environment. 
   Doing so will activate any libraries that a user has installed 
   using this virtual environment (such as Django)

5. Once VE has been initialized, install Django: `pip install Django`

6. Install [MariaDB](https://downloads.mariadb.org/)

7. Install on Virtual Enviornment `mysqlclient` with [file](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
   
   Note: Once file has been downloaded go to file location and initialize the VE.
   Run command: `pip install <filename>`

  * If an error occurs regarding C++ 14.0 dependencies click link to install [C++ 14.0 Build Tools](https://go.microsoft.com/fwlink/?LinkId=691126)
    * If Error persists, Link up C++ 14.0 to your `PATH` variable:
      1. `C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin`
      2. `C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE`

9. Go to `retroGame/retroGame/settings` and change DATABASE to

~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'NAME': '$DATABASE',
        'PASSWORD': '$PASSWORD',
        'PORT': '3306',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
~~~

  * `$DATABASE`: Database in your MariaDB server
  * `$PASSWORD`: Password for the root user

8. Run the Django Server: `python manage.py runserver`
## Simple Django commands
  * Start the django server on localhost: `python manage.py runserver`
  * Accessing django shell for database: `python manage.py shell`
  * If database has changed: `python manage.py inspectdb > retoGameWeb/models.py`

### Django Documentation & Tutorial
  * [Django](https://docs.djangoproject.com/en/2.0/)
  * [Django with legacy Databases](https://docs.djangoproject.com/en/2.0/howto/legacy-databases/)