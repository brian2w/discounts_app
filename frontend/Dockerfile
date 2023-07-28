# Use the official Flutter image as the base image
FROM cirrusci/flutter

# Set the working directory
WORKDIR /app

# Copy the contents of the frontend directory to the working directory in the container
COPY . .

# Build the Flutter app
RUN flutter build web