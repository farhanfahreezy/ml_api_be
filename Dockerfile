# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the Pipfile and Pipfile.lock (if it exists)
COPY Pipfile Pipfile.lock* ./

# Install pipenv
RUN pip install pipenv

# Install dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of your application code
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port your app runs on
EXPOSE 5000

# Command to run your Flask application
CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
