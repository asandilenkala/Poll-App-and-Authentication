Poll Application with User Authentication

This project extends the basic functionality of a poll application by adding user authentication features. Users must register and log in before they can participate in voting.

Features:

1. User Registration:
        A new user registration page allows users to sign up with a username, password, and first name.
2. User Login:
        A login page where registered users can log in using their credentials.
3.Voting Restriction:
        Users must be logged in to vote in polls. This ensures that only authenticated users can participate.

Installation:

1. Clone the repository:

> git clone https://github.com/asandilenkala/Poll-App-and-Authentication.git
> cd poll-app

2. Install dependencies: Make sure you have Python and Django installed. Install the necessary packages using:

> pip install -r requirements.txt

3. Set up the database: Run the following commands to create the necessary database tables:

> python manage.py makemigrations
> python manage.py migrate

4. Create a superuser (optional): If you want to access the Django admin interface, create a superuser by running:

> python manage.py createsuperuser

5. Run the development server: Start the Django development server:

> python manage.py runserver

6. Access the application: Open your web browser and go to http://127.0.0.1:8000/ to access the poll application.

Usage:

1. Register a New User:
> Navigate to the registration page to create a new account.

2. Login:
   > After registering, go to the login page and sign in with your credentials.

3. Vote in Polls:
> Once logged in, you can participate in any available polls.

4.Logout:
> You can log out after participating in the polls.

Contributing:

If you'd like to contribute to this project, please fork the repository and submit a pull request.

License:

> This project is open-source and available under the MIT License.

