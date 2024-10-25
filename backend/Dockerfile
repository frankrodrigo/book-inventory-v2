# backend/Dockerfile

# Stage 1: Build Stage (Install dependencies)
FROM python:3.9-alpine as build

# Set the working directory in the container
WORKDIR /app

# Install build dependencies for compiling any packages
RUN apk add --no-cache gcc g++ unixodbc-dev

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Stage (Copy only required files)
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy installed dependencies from build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the rest of the app's source code
COPY . /app

# Expose the Flask app's port
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
