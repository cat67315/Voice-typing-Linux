#!/bin/bash

PY_PATH="$(realpath ../main.py)"

if [ -d "~/snap/firefox/common/.mozilla" ]; then
mkdir ~/snap/firefox/common/.mozilla/native-messaging-hosts
cat <<EOF > ~/snap/firefox/common/.mozilla/native-messaging-hosts/com.cat67315.Vtl.json
{
  "name": "com.cat67315.Vtl",
  "description": "Voice typing Linux messaging service",
  "path": "$PY_PATH",
  "type": "stdio",
  "allowed_extensions": [
    "<EXTENSION_ID>@domain"
  ]
}
EOF
elif [ -d "~/.mozilla" ]; then
mkdir ~/.mozilla/native-messaging-hosts
cat <<EOF > ~/.mozilla/native-messaging-hosts/com.cat67315.Vtl.json
{
  "name": "com.cat67315.Vtl",
  "description": "Voice typing Linux messaging service",
  "path": "$PY_PATH",
  "type": "stdio",
  "allowed_extensions": [
    "<EXTENSION_ID>@domain"
  ]
}
EOF
else
    echo "ERROR_CODE_1: Firefox is not installed. Please install Firefox and run it once then try again. If this keeps happening, refer to the README file."
    echo "Press any key to end..."
    read -n 1 -s
fi