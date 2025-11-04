# Dockerfile
# Example Dockerfile for running the Express demo
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
EXPOSE 3000
CMD ["node", "express_server.js"]
