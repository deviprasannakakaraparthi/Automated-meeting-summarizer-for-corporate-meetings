# Use a Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Command to run the app
CMD ["python", "backend/app.py"]

