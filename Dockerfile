# Start with a base image
FROM openjdk:19-jdk-slim

# Set the working directory to /app
WORKDIR /demo

# Copy the JAR file into the container
COPY target/demo-0.0.1-SNAPSHOT.jar /demo/demo-0.0.1-SNAPSHOT.jar

# Expose port 8080
EXPOSE 8080

# Set the command to run when the container starts
CMD ["java", "-jar", "demo-0.0.1-SNAPSHOT.jar"]