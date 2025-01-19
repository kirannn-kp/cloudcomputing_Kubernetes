# Use Python 3.9 image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the API files into the container
COPY . /app

# Install required dependencies
RUN pip install flask
RUN pip install flask-cors

# Expose port 8080 for the API
EXPOSE 5000

# Run the Flask API
CMD ["python", "app.py"]
