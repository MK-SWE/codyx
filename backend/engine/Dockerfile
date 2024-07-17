# Use an official alpine runtime as a parent image
FROM alpine:latest
# Set the working directory in the container
WORKDIR /usr/src/app
# Copy the DockerSetup.sh script into the container at /usr/src/app
COPY DockerSetup.sh /usr/src/app/
# Install needed packages
RUN sh DockerSetup.sh
# Clean up by removing the setup script
RUN rm DockerSetup.sh