#!/bin/bash
# Sends a GET request and return response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
