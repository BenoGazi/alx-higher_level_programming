#!/bin/bash
#Takes the URL as an argument, sends GET  request to the URL
curl -sH "X-School-User-Id: 98" "$1"
