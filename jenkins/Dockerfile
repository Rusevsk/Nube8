FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt-get update && apt-get install -y docker.io
# Instalar docker-compose
RUN curl -L "https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose
USER jenkins