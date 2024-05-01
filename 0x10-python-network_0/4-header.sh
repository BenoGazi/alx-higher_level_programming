#!/bin/bash
#Takes the URL as an argument, sends GET  request to the URL
#+and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
