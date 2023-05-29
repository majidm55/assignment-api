# assignment
Get Engagement Report

#
This is a Flask project built using Flask framework and several additional libraries. It provides a RESTful API with Swagger documentation.

## Requirements

- Python 3.7 or higher
- Flask 2.2.2
- Connexion with Swagger UI 2.14.1
- Flask-Marshmallow with SQLAlchemy support 0.14.0
- Flask-SQLAlchemy 3.0.3
- Marshmallow 3.19.0
- Marshmallow-SQLAlchemy 0.29.0

## Installation

1. Make sure you have Python 3.7 or higher installed (3.11.0 preferred)
2. Clone this repository: `git clone https://github.com/majidm55/assignment-api.git`
3. Navigate to the project directory: `cd assignment_api`
4. Create a virtual environment (optional but recommended): `python -m venv /path/to/new/virtual/environment`
5. Activate the virtual environment
6. Install the required dependencies: `pip install -r requirements.txt`

## Configuration

1. Open the `config.py` file and update the configuration settings according to your environment.

## Usage

1. Run the Flask application: `python app/assignment-api.py`
2. Open your web browser and go to `http://localhost:8000` to access the API and Swagger documentation.

## Project Structure

- `app.py`: Entry point of the application.
- `config.py`: Configuration file for the application.
- `controllers/`: Contains the API controllers which call the models.
- `models/`: Contain the models which define data
- `databases/`: References to adding data .
- `templates/`: Contains HTML templates to render locally.
