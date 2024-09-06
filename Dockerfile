# Use the official Python image from the Docker Hub
FROM python:3.11.9

# Set the working directory in the container
WORKDIR /app
COPY start.sh .
RUN chmod +x start.sh


# Copy the requirements file into the container
COPY requirements.txt .

# Run the start script
CMD ["./start.sh"]

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code and the start script into the container
COPY . .


# Make sure the start script is executable


# Set the environment variable to indicate Flask is running
ENV FLASK_APP=app.py

# Expose the port that Flask will run on
EXPOSE 5000


CMD flask run --host=0.0.0.0 && echo "Flask application started."