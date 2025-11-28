# Use official Python base image
FROM python:3.13-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project
COPY . .

# Expose Flask default port
EXPOSE 5000

# Command to run Flask app
CMD ["python", "app.py"]
