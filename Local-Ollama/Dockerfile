# Use a lightweight Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install Flask and Flask-CORS
RUN pip install flask flask-cors
RUN pip install requests

# Expose the port
EXPOSE 6002

# Run the application
CMD ["python", "app.py"]
