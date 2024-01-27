# Use an official Node runtime as a parent image
FROM node:20

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install any needed packages specified in package.json
RUN npm install

# Bundle app source inside the Docker image
COPY . .

# Make port 3030 available to the world outside this container
EXPOSE 3030

# Set environment variables
ENV PORT=3030

# Define environment variable
ENV NODE_ENV=production

# Build the app
RUN npm run build

# Run the app when the container launches
CMD ["npm", "run", "start"]
