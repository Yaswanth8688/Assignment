-->Assignment Project

This project, Assignment, is a Django-based application designed to manage user data. It provides views to add, list, and view individual user details in a clean and responsive format.

-->Features

Home Page: A simple greeting page.
User List: Displays all users in a table format.
Single User: Shows details of a single user in a table format.
Add User: Provides a form to add a new user.

-->Technologies Used

Python (Django Framework)
HTML with Internal CSS and JavaScript
SQLite (Default Django Database)
Responsive design for mobile and desktop views.

-->Project Structure

assignment/
├── environment/         # Virtual environment
├── assignment/          # Main Django project
│   ├── settings.py      # Django settings
│   ├── urls.py          # Project-level URL configuration
│   └── ...
├── myapp/               # Application folder
│   ├── models.py        # Database models
│   ├── views.py         # Views for handling requests
│   ├── forms.py         # Django forms
│   ├── templates/       # HTML templates
│   │   ├── base.html    # Base template for consistent design
│   │   ├── hello.html   # Template for the home page
│   │   ├── users.html   # Template to display all users
│   │   ├── single_user.html  # Template for a single user's details
│   │   ├── new_user.html     # Template for adding a new user
│   └── ...
└── README.md            # Project documentation

-->Setup Instructions

1. Clone the Repository
git clone <repository-url>
cd assignment

2. Create and Activate Virtual Environment

python -m venv environment       
environment\Scripts\pip install django  #Install django in scripts folder 
source environment/bin/activate  # On macOS/Linux
environment\Scripts\activate     # On Windows activate environment

3. Apply Migrations
python manage.py makemigrations
python manage.py migrate

4. Run the Development Server
python manage.py runserver
Visit http://127.0.0.1:8000/ to access the application.

-->Usage

Home Page
Visit the root URL to see the "Hello, World!" greeting.

View All Users
Navigate to the "All Users" page from the menu to see a table of all users.

View a Single User
Click the "View" button next to a user in the table to see their details.

Add a New User
Navigate to the "Add User" page to add a new user to the system.


-->Models

The users model is defined in models.py:
//Desiging a table "users" with the following columns:
--id (int primary key)
--name (varchar)
--email (varchar)
--role (varchar)

class users(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    
-->Forms
The userForm in forms.py maps directly to the users model:
class userForm(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'

-->HTML Templates
All templates are stored in the templates/ folder and are designed with responsive internal CSS for a better user experience.

-base.html: Base template with navigation.
-hello.html: Welcome page.
-users.html: Displays all users in a table.
-single_user.html: Displays details of a single user in a table.
-new_user.html: Provides a form to add a new user.

-->Styling and Responsiveness
-Internal CSS ensures a cohesive look across pages.
-Tables and forms are styled for clarity and functionality.
-Mobile responsiveness is achieved using media queries.

-->License
This project is for educational purposes and does not include a license.

