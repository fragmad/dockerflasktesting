====================
Docker Flask Testing
====================

This is a project for me futz around with and keep various Docker, Flask, and
Testing examples in one place.

Please do not assume that anything in this is best practice.

===============
How To Do Stuff
===============

1. How to Build the Docker Image::

   docker build -t myapp/hellos ./

2. How Run the Docker Image as a Dev Server::

   docker run -d -p 80:5000 myapp/hellos

or I find this more useful since it expose the logs to the terminal.::

  docker run -it -p 80:5000 myapp/hellos

3. How to Run Unit Tests::

  docker run -it -p 80:5000 myapp/hellos python tests/*

4. How to Run Behaviour Tests::

  docker run -it -p 80:5000 myapp/hellos behave

5. How to Run Bash::

  docker run -it -p 80:5000 myapp/hellos behave

