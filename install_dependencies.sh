#!/bin/bash

# Check if pip3 is installed
if not command -v pip3 >/dev/null 2>&1; then
    echo "pip3 is not installed. Installing pip3..."
    # Checks for package managers and installs pip3 accordingly
    if command -v apt >/dev/null 2>&1; then
        sudo apt update
        sudo apt install python3-pip
    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf check-update
        sudo dnf install python3-pip
    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -Syu
        sudo pacman -S python-pip
    else
        echo "No supported package manager found. Please install pip3 manually."
        exit 1
    fi
fi
# Install required Python packages
pip3 install -r requirements.txt