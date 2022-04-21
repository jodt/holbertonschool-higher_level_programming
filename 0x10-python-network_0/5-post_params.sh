#!/bin/bash
#script that takes in a URL, sends a POST, and displays the body of the response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"; echo ""
