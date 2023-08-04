# University Course Catalog Web Application

Welcome to the University Course Catalog Web Application! This project aims to provide a user-friendly interface for exploring, searching, and planning courses offered at the University of Illinois at Urbana-Champaign.

## Project Overview

The University Course Catalog Web Application offers an extensive collection of features designed to assist users in navigating the vast course offerings at the University of Illinois at Urbana-Champaign. With over 3800 courses available, the application provides a seamless experience for searching, retrieving detailed information, and planning academic schedules.

## Project Workflow

The University Course Catalog Web Application functions seamlessly to enhance the user experience:

1. Users interact with the search box, prompting the JavaScript code to send an AJAX request to the server's /search route.
2. The server processes the search query and responds with search results.
3. When users click the "Plan" button, the JavaScript code sends an AJAX request to the server's /show route with the selected course IDs.
4. The server responds with detailed course information, and the Jinja2 templates dynamically generate HTML content based on the received data.
5. The combination of Flask's server-side capabilities and JavaScript's client-side interactivity results in a seamless user experience for exploring and planning university courses.

### Features

- **Search:** Effortlessly search through over 3800 University of Illinois at Urbana-Champaign courses using the integrated search functionality.
- **Course Details:** Access comprehensive information about each course, including its description, prerequisites, instructor details, grade distribution, and general education requirements.
- **Planning:** Select courses for planning purposes, allowing users to curate their academic schedules with ease.
- **User-friendly Interface:** A well-designed and intuitive user interface ensures a smooth and informative browsing experience.

## Technologies Used

The University Course Catalog Web Application is built using a combination of programming languages, frameworks, and libraries to create a robust and interactive platform.

- **Programming Languages:** Python, JavaScript, HTML, CSS
- **Web Framework:** Flask
- **Libraries:** jQuery, AJAX
- **Data Processing:** pandas, json

## Getting Started

Follow these steps to set up and run the application on your local machine:

1. Clone this repository: `git clone https://github.com/your-username/your-repo.git`
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Flask application: `python app.py` or `flask run`
4. Open your web browser and navigate to `http://localhost:5000` to access the web application.

## Routes and Templates

### Root Route (/)

The root URL of the website.

- Renders a template named "layout.html" to provide a basic layout for the site.

### Search Route (/search) - POST and GET methods

Handles user search requests for courses.

- Utilizes AJAX to send a request to the server to search for matching courses based on the user's query.
- Renders a template to display the search results.

### Show Route (/show) - POST and GET methods

Handles the display of selected courses for planning.

- Utilizes AJAX to send a request to the server with selected course IDs.
- Renders a template to display detailed information about the selected courses.

## Data Processing

The project utilizes data from various sources to provide accurate and detailed course information.

- `class_hierarchy.json`: Contains course hierarchy and prerequisites data.
- `all_gened.json`: Contains general education requirements data.
- `grade_per_section.json`: Contains grade distribution and instructor details data.

## Contribution

Contributions to this project are welcome! If you encounter issues or have suggestions for enhancements, please feel free to submit a pull request or open an issue.

## Author Information

Name: Lawrence Granda Zarzuela

Project Duration: February 2023 to July 2023
