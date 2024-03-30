#!/bin/bash
#Scripts that sneds a DELETE request to the url
curl -s -I -X OPTIONS "$!" | grep "Allow:"| cut -f2 -d" "
