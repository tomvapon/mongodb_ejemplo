# Use the official MongoDB image
FROM mongo:latest

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the MongoDB configuration file (if you have a custom config)
# COPY ./mongod.conf /etc/mongod.conf

# Expose the default MongoDB port
EXPOSE 27017

# Start MongoDB when the container starts
CMD ["mongod"]
