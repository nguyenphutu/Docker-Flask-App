# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for certain Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev  # Nếu bạn sử dụng PostgreSQL hoặc psycopg2

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip  # Nâng cấp pip để tránh các lỗi cũ
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run flask when the container launches
CMD ["flask", "run --reload", "--host=0.0.0.0"]
