#!/bin/bash

# install chromedriver

curl -SL https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chromedriver-linux64.zip > chromedriver.zip

unzip chromedriver.zip

rm chromedriver.zip

mv chromedriver-linux64/* .

rm -rf chromedriver-linux64

# install chrome binary

curl -SL https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chrome-headless-shell-linux64.zip > chrome-headless-shell.zip

unzip chrome-headless-shell.zip

rm chrome-headless-shell.zip

mv chrome-headless-shell-linux64/* .

rm -rf chrome-headless-shell-linux64