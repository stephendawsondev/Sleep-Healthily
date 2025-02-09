# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9.17

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /sleep_healthily

RUN mkdir -p /var/log/django

# Copy the current directory contents into the container at /sleep_healthily
COPY . /sleep_healthily/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js dependencies if package.json exists
RUN if [ -f package.json ]; then npm install; fi

# Make port 3004 available to the world outside this container
EXPOSE 3004

# Run the application using Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:3004", "--access-logfile", "-", "--error-logfile", "-", "sleep_healthily.wsgi:application"]
