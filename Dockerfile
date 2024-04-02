# Use an official Python runtime as a parent image
FROM python:3.10.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache/pip

# Copy the current directory contents into the container at /code/
COPY . /code/

# Expose port 8000 on the container
EXPOSE 8000
