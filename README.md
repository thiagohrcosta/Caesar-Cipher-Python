# Caesar Cipher

## Technologies used
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

This project was created using Docker to studying the basic concepts of Python learned at day 08  in the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)**. 

## Summary
**Day 08**: Learn more about functions. 

## What user can do?

**User:** Can add a word and type how many shifts he wants. After that a encrypt function will be called. User can also decrypt a word. 

## How to run this project
This project was created with Docker, the Dockerfile is:

    FROM  python:3
    
    WORKDIR  /app
    
    COPY  .  .
    
    CMD  ["python",  "app/main.py"]

To run just download this project and run the follow commands:  `docker build -t caesar-cipher .`  then run `docker run -it caesar-ciper`. )
