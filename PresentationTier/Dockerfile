# Use Nginx image from Docker Hub
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy the HTML file to the Nginx container
COPY index.html .

# Copy the Dockerfile for documentation purposes
COPY Dockerfile .

# Expose port 80
EXPOSE 80
