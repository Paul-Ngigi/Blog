# BLOGGERS
## Author

[Paul-Ngigi] https://github.com/Paul-Ngigi

# Description
This  is a flask application that allows users to post blogs and also allows other users who have signed up to comment on the blogs. It also allows a person to signup to be able to access the functionalities of the application


## Installation Instruction
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/Paul-Ngigi/Blog.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd Blog
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.9 manage.py server
  ```
5. Testing the application
  ```bash
  python3.9 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.9](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at paulkush7777@gmail.com

## License
* *MIT License*