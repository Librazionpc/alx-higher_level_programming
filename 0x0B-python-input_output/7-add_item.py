#!/usr/bin/python3
"""Dealing Scripts"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = add_item.json

try:
    existing_content = load_from_json_file(file_name)
except FileNotFoundError:
    existing_content = []
existing_content.extend(sys.argv[1:])

save_to_json_file(existing_content, filename)
