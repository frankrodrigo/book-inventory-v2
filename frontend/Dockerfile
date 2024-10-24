# frontend/Dockerfile
# Use an official Node.js image
FROM node:14

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app's source code
COPY . .

# Build the Vue.js app
RUN npm run build

# Install a lightweight web server to serve the built files (e.g., serve)
RUN npm install -g serve

# Expose port 5000 (or the one you use for Vue.js)
EXPOSE 3000

# Serve the app
CMD ["serve", "-s", "dist"]
