# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Gradio app
EXPOSE 8000

# Ensure the environment variables are loaded properly
ARG GROQ_API_KEY

ENV GROQ_API_KEY=$GROQ_API_KEY

# Run the app when the container launches
CMD ["python", "main.py"]
