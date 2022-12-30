#!/bin/bash
# Displays the size of the body of the taken URL in Bytes
curl -s "$1" | wc -c
