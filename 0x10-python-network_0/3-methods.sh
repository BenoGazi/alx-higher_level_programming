#!/bin/bash
# Gets the allowed methods in a server if available through the OPTIONS resquest
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
