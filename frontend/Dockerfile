FROM node:10-alpine

RUN echo 'cd /app; umask 000; npm install && npm start' > /tmp/npm_install_and_start.sh

WORKDIR /app

ENTRYPOINT /bin/ash /tmp/npm_install_and_start.sh