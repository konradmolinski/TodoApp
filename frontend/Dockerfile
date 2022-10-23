FROM node:lts-alpine3.16

WORKDIR /app

COPY . .

RUN npm i
RUN npm run build
CMD ["npm", "run", "preview"]
