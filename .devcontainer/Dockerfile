FROM mcr.microsoft.com/devcontainers/python:1-3.13-bookworm

# Remove o repositório do Yarn que está quebrando o apt-get update
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && rm -f /etc/apt/sources.list.d/nodesource.list \
    && apt-get update