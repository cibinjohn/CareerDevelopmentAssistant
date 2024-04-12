# Use a specific version of Node
FROM node:lts-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
#RUN npm install

# Copy local code to the container image
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Run the web service on container startup
CMD ["npm", "start"]
#CMD tail -f /dev/null
