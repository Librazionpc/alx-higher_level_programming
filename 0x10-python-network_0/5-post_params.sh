#!/bin/bash
#Scripts that POST to an email address with a body
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
