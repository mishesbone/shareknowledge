
ShareKnowledge is a social media web application designed to enable users to publish articles, upload offline media, record live media, and connect with like-minded individuals. The platform fosters knowledge sharing, networking, teaching, and mentoring while providing tools for personal development.

Table of Contents
Features

Technologies Used

Installation

Usage

Contributing

#License#

Features
User Registration & Login: Secure authentication system using hashed passwords.
Dashboard: A collapsible sidebar interface for easy navigation.
Media Uploads: Support for images, audio, and video uploads.
Personal Development Section: Tools and resources for self-improvement.
Knowledge Sharing: Publish articles, connect with others, and mentor online.

Technologies Used
Backend Framework: Python (Flask)
Database: SQLite (via SQLAlchemy)
Frontend: HTML, CSS, JavaScript
File Handling: Flask-Uploads
Form Validation: Flask-WTF



Installation
Clone the Repository:

git clone https://github.com/your-username/shareknowledge.git
cd shareknowledge

Set up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Configure the Application: Modify the settings in config.py if necessary (e.g., database URI or file upload path).

Initialize the Database:

python app.py
This will create the SQLite database file (shareknowledge.db) in the project directory.

Run the Application:

python app.py

Usage

Register a new account.
Log in to access your dashboard.
Explore features such as media uploads, personal development resources, and knowledge-sharing tools.
Use the collapsible sidebar to navigate between different sections.
Access the app at http://127.0.0.1:5000


Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m "Add new feature".
Push to the branch: git push origin feature-name.
Create a pull request.

License
This project is licensed under the MIT License.

Future Enhancements
Live streaming functionality.
Advanced networking features such as group discussions and mentoring sessions.
Integration with external APIs for analytics and insights.
Enhanced personal development resources.
