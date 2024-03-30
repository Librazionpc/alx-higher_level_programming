#!/bin/bash
#Scripts that sneds a DELETE request to the url
curl -s -I -X OPTIONS "$1" | grep "Allow:"| cut -f2- -d" "
