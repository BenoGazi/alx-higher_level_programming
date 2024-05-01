#!/bin/bash
#Script posts Json data files and tests a server
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
