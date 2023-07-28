# Use the official Python image as the base image
FROM python:3

# Set the working directory
WORKDIR /app

# Copy the contents of the backend directory to the working directory in the container
COPY . .

# Install Django and other required dependencies
RUN pip install -r requirements.txt

# Run Django server (you can replace "your_app_name" with the name of your Django app)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]