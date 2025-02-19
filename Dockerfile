# Use a base image with Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file (if available) and install the dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files from your local directory to the container
COPY . /app

# Command to run when the container starts
CMD ["python", "app.py"]

# Expose port 5000 for the application
EXPOSE 5000

