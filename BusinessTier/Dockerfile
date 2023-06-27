# Use Python image from Docker Hub
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application to the container
COPY app.py .

# Expose port 80
EXPOSE 80

# Start the Flask application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
