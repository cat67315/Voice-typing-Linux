#!/bin/bash

# Check if pip3 is installed
if ! command -v pip3 >/dev/null 2>&1; then
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
        echo "No supported package manager found. Please install pip3 manually then rerun"
        exit 1
    fi
fi

# Check if venv is instaled and create a virtual environment if present
if [ ! -d "venv" ]; then
    python3 -m venv venv
    if [ $? -eq 0 ] && [ -d "venv" ]; then
        echo "Venv successfully created."
    else
       echo "Venv is not installed. Installing venv..."
        if command -v apt >/dev/null 2>&1; then
            sudo apt update
            sudo apt install python3-venv
        elif command -v dnf >/dev/null 2>&1; then
            sudo dnf check-update
            sudo dnf install python3-venv
        elif command -v pacman >/dev/null 2>&1; then
            echo "ERROR: Venv is not instaled but shoud be included with python package in pacman based distros. I onstly dont even know what to do here. Maby try reinstaling python?"
            exit 1
        else
            echo "No supported package manager found. Please install venv manually then rerun"
            exit 1
        fi
        # Try to create the virtual environment again
        python3 -m venv venv
        if [ $? -eq 0 ] && [ -d "venv" ]; then
            echo "Venv successfully created."
        else
            echo "Failed to create virtual environment even after installing venv. Please check your Python installation."
            exit 1
        fi
    fi
fi

# Install required Python packages inside a virtual environment
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt