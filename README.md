# WeRateMovies
----------
### Main Goal ###
Creating a website that permits to rate, share and recommend stuff.    
A simple version is currently in development and closed to only two people to rate things.    
In a more advanced version other users will be able to register and rate stuff too.

### Secondary Goal ###
Through the processing of creating this website I want to go further in the learning of Flask and its plugins. For example I'd like to create an administration interface (using Flask-Admin) which would work with Flask-Login flawlessly. The management of the database will also be a bit more complex, using Many-To-Many fields, forcing me to dig deeper in the Flask-SQLAlchemy plugin and learning how to achieve the main goals of the application.

### Technologies ###
This website will be created using the Flask micro-framework. It will need some additionnal plugins such as Flask-Login to handle users.

### Planned Steps ###
#### First : Backend Development ####

 - Database creation
 - User management
 - Admin interface
 - User management implementation for admin interface

#### Second : Frontend Development ####

 - Simple web interface
 - Image management
 - Improving the admin interface


### Excluded files and such ###
Of course as this project may be in production one day, the files containing the sensitive data will be excluded from the project.     
For example the `config.py` file and `manage.py` contains sensitive informations such as the Private Key used for sessions and CSRF Protection.    
So if you want to use that code you'll have to create your own files. To help you out I created a python script that can be used to create a sample project in one command line. You can find this project [here][1] and a little demonstration below:

[![asciicast](https://asciinema.org/a/10051.png)](https://asciinema.org/a/10051)


  [1]: https://github.com/Depado/flask-skeleton
