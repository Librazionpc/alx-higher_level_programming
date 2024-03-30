#!/bin/bash
#Scripts that takes in a url and return the size of the body of the response

curl -sI "$1" | grep i "Content-lenght" | cut -d " " -f 2 
