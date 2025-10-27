#!/bin/bash

PY_PATH="$(realpath ../main.py)"

if [ -d "~/.config/google-chrome/NativeMessagingHosts" ]; then
cat <<EOF > ~/.config/google-chrome/NativeMessagingHosts/com.cat67315.Vtl.json
{
  "name": "com.cat67315.Vtl",
  "description": "Voice typing Linux mesaging service",
  "path": "$PY_PATH",
  "type": "stdio",
  "allowed_origins": [
    "chrome-extension://<EXTENSION_ID>/"
  ]
}
EOF
else
    echo "ERROR_CODE_0: Chrome is not installed. Please install Chrome and run it once then try again. If this keeps happening, refer to the README file."
    echo "Press any key to end..."
    read -n 1 -s
fi