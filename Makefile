name: CI
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Environment Variables
        run: |
          echo "SERVER_HOSTNAME=${{ secrets.SERVER_HOSTNAME }}" >> $GITHUB_ENV
          echo "HTTP_PATH=${{ secrets.HTTP_PATH }}" >> $GITHUB_ENV
          echo "ACCESS_TOKEN=${{ secrets.ACCESS_TOKEN }}" >> $GITHUB_ENV
      - name: install packages
        run: make install
      - name: lint
        run: make lint
      - name: format
        run: make format
      - name: test
        run: make test