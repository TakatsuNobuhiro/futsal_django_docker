FROM node:14-alpine3.11

RUN mkdir -p /workspace
WORKDIR /workspace

ENV NODE_ENV=development

RUN npm install
RUN npm i @nuxtjs/axios


EXPOSE 3000