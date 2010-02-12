#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(dirname "$0")
exec python faketwitter/tests/__init__.py
