# Use the official Python 3.10.12 image as a base
FROM python:3.10.12

# Set the working directory inside the container
WORKDIR /app

# Copy necessary files into the image
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Default command to run the application
CMD ["python", "-m", "api.v1.app"]
