#!/bin/sh
pytest core/tests/test_contents.py

python package_statistics.py amd64