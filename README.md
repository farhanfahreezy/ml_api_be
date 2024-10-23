# Machine Learning API Backend

This project is a Flask-based backend API with PostgreSQL as the database, utilizing SQLAlchemy ORM and Alembic for database migrations. It also incorporates JWT for authentication, CORS handling, and basic machine learning functionality via scikit-learn.

# Features

### Endpoints:

- `/train`: Train a machine learning model.
- `/predict`: Predict based on trained models.
- `/status`: Check the status of the training/prediction tasks.
- `/auth/sign-in` : Sign in using credentials.
- `/auth/sign-up` : Register user
- Swagger UI: You can test these API endpoints via the Swagger docs, available at `localhost:5000/api-docs`.

# Requirements

- Python 3.10
- PostgreSQL (ensure it's running before starting the app)

# Dependencies

Dependencies are managed using Pipenv. The main dependencies include:

- Flask: Web framework.
- psycopg2-binary: PostgreSQL database adapter.
- Flask-Swagger-UI: Provides Swagger documentation UI.
- Flask-RESTful: For building REST APIs.
- scikit-learn: For machine learning functionalities.
- Alembic: For handling database migrations.
- SQLAlchemy: ORM for database interactions.
- Flask-Migrate: Extension for handling SQLAlchemy database migrations with Alembic.
- Werkzeug: Comprehensive WSGI web application library.
- bcrypt: For password hashing.
- Flask-JWT-Extended: For handling JWT authentication.
- Flask-CORS: For Cross-Origin Resource Sharing.

For development:

- pytest: Testing framework.

# Setup Instructions

Follow these steps to set up and run the project locally:

1. Clone the repository:

```
bash
git clone <repository-url>
cd <repository-directory>
```

2. Create and activate a virtual environment using pipenv:

```
bash
pipenv shell
```

3. Install dependencies:

```
bash
pipenv install
```

4. Create a .env file based on the .env.example:

```
bash
cp .env.example .env
```

Make sure to fill in the required environment variables like database credentials, JWT secret key, etc.

5. Set up the database: Ensure that PostgreSQL is running and the database is set up according to the configuration in your .env file.

6. Run migrations to apply any existing database schema:

```
bash
flask db upgrade
```

7. Run the application:

```
bash
flask run
```

The server will start, and the API will be available at http://localhost:5000/.

Access Swagger documentation: Open http://localhost:5000/api-docs in your browser to interact with the available API endpoints.

# Running Tests

To run the tests using pytest:

```
bash
pytest
```
