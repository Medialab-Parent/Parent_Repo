#!/bin/bash

# Function to open a new terminal tab and run a command
open_new_tab() {
    osascript <<EOF
tell application "Terminal"
    do script "$1"
end tell
EOF
}

# Set the FLASK_APP_DIR to the current directory path
export FLASK_APP_DIR="$(pwd)"

# Commands to run in each service's directory
CMD1="cd '$FLASK_APP_DIR/AI_API-Wrapper' && nodemon --exec python3 llm_backend.py"
CMD2="cd '$FLASK_APP_DIR/AI_Filter' && nodemon --exec python3 twitterRoberta.py"
CMD3="cd '$FLASK_APP_DIR/AI_Server' && nodemon --exec python3 server.py"
CMD4="cd '$FLASK_APP_DIR/AI_Database' && nodemon --exec python3 database.py"

# Open new Terminal tabs for each command
open_new_tab "$CMD1"
open_new_tab "$CMD2"
open_new_tab "$CMD3"
open_new_tab "$CMD4"

echo "Services are starting in separate terminal tabs..."