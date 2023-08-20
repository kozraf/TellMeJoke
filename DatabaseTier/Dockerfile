# Use the official MySQL image as a base
FROM mysql:latest

# Add the init.sql script to the Docker image
COPY init.sql /docker-entrypoint-initdb.d/
