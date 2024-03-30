#!/bin/bash
#Scripts that POST to an email address with a body
curl -s "$1" -X POST "email=test@gmail.com&subjec=I will always be here for PLD"
