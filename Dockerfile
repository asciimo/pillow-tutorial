FROM python:alpine3.10

RUN apk add --no-cache build-base zlib-dev jpeg-dev
RUN pip install Pillow

WORKDIR /pillow-tutorial

# Create a user with the same UID as the host user, to ensure files
# created by the container are accessible to the host user.
ARG uid
RUN adduser -DH --gecos "Pillow tutorial user" -u ${uid} pillowtut 
USER pillowtut

