#!/bin/bash
#Script that GET usgin a header varaible the bodey of rhe http response
curl -s "$1" -H "X-School-User-Id: 98"
