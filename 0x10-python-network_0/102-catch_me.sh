#!/bin/bash
# Breaks to the http on holberton serverd and displays "You caught me"
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
