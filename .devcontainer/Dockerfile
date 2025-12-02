# Base image with Python 3.11 and VS Code devcontainer features
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install Bazelisk (a wrapper that always fetches the right Bazel version)
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -L https://github.com/bazelbuild/bazelisk/releases/download/v1.19.0/bazelisk-linux-amd64 \
    -o /usr/local/bin/bazel && \
    chmod +x /usr/local/bin/bazel

# Set working directory inside the container
WORKDIR /workspaces/ml-autonomous-car