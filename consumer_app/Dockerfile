# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install kafka-python python-dotenv

# Copy custom hosts file into container
COPY hosts /etc/hosts

# Run consumer.py when the container launches
CMD ["python", "consumer.py"]
