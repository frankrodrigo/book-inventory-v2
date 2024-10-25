# frontend/Dockerfile

# Stage 1: Build Stage
FROM node:14-alpine as build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app's source code
COPY . .

# Build the Vue.js app with the environment variable
ARG VUE_APP_BACKEND_URL
ENV VUE_APP_BACKEND_URL=${VUE_APP_BACKEND_URL}
RUN npm run build

# Stage 2: Serve Stage with Nginx
FROM nginx:alpine

# Copy the built files from the build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 (nginx default port)
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
