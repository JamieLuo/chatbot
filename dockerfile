FROM node:12

WORKDIR /dockerApp

COPY *.py ./

RUN npm install

COPY . .

Env PORT=8080

EXPOSE 8080

CMD ["npm","start"]