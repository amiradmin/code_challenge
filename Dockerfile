# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run migrations and create a superuser
CMD ["sh", "-c", "python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:8000"]
