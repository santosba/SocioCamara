FROM node:16

WORKDIR /front

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project files
COPY . .

# Install Vue CLI globally
RUN npm install -g @vue/cli

# Set npm registry to faster mirror and install dependencies
RUN npm config set registry https://registry.npmmirror.com
RUN npm install axios vuex vue-router

EXPOSE 8080
CMD ["npm", "run", "serve"]