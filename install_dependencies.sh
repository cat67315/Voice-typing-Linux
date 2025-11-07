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

# Check if venv is instaled
python3 -m venv venvtest
if [ $? -eq 0 ] && [ -d "venvtest" ]; then
    rm -rf testvenv
else
    echo "Venv is not installed. Installing venv..."
    if command -v apt >/dev/null 2>&1; then
        sudo apt update
        sudo apt install python3-venv
    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf check-update
        sudo dnf install python3-venv
    elif command -v pacman >/dev/null 2>&1; then
        echo Warning: Since you are on arch/manjaro venv is not a thing. It will use virtualenv as a substatute but I do not use arch/manjaro so I do not know if it will work properly.
        read -p "Press [Enter] to continue or ^C to quit"
        sudo pacman -Syu
        sudo pacman -S python-virtualenv
    else
        echo "No supported package manager found. Please install venv manually then rerun"
        exit 1
    fi
fi


# Install required Python packages inside a virtual environment

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt