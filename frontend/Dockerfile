FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

# Add this line to copy the public folder with the index.html file
COPY public /usr/src/app/public

EXPOSE 3000

CMD [ "node", "index.js" ]
