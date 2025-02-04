#!/bin/bash

# Update package list
sudo apt update

# Install make for managing build automation
sudo apt install make -y

# Install Python virtual environment package
sudo apt install python3.12-venv -y

# Install tree for listing directories in tree format
sudo apt install tree -y

echo "VM setup completed successfully!"

