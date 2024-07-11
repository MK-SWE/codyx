# Use an official Python runtime as a parent image
FROM alpine:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the solutions/ directory contents into the container at /usr/src/app
COPY solutions/ /usr/src/app/solutions/
COPY DockerSetup.sh /usr/src/app/

# Install needed packages
RUN sh DockerSetup.sh
RUN rm DockerSetup.sh
