# L3T11
Hyperiondev Task - Introduction to Natural Language Processing

## Requirements
1. Python 3 - https://www.python.org/downloads/

## Installation
If you are working in a virtual environment open that before following these steps

1. Clone the repository to your pc
2. In command prompt navigate to the root directory for the repository
3. In command prompt enter 'pip install -r requirements.txt' to download required packages

## Usage
You can run the script by entering 'python gardens.py' in command prompt from the root directory for the local repository.

The output should look like this:

![garden py output](https://user-images.githubusercontent.com/15369629/221439149-67230b0f-ce2d-46c3-b08e-3b101708658e.PNG)

## Running in a container
You can also create an image using the included Dockerfile to to run the script a container.
To do this you will either need to install Docker Decktop (https://www.docker.com/) or creat an account on Docker and use Docker Playground (https://labs.play-with-docker.com/)

### To run with Docker Desktop
1. Using command line in the root directory for the project (where the Dockerfile is found) run - 'docker build -t [tag] ./' where [tag] is whatever name you want to use for the image
2. Once this has finished you can now runt the image in a container by entering - 'docker run [the tag you chose]'

### To run in docker playground
1. Follow step 1 from the Docker Desktop instructions to build the image.
2. In command line enter 'docker login' and enter your login details for docker hub.
3. On docker hub you will need to create a repository and then retag the local image to match your repository's name.
   to do this in command line run - 'docker tag [tag] [user]/[repo]' where [tag] is the name you chose when building the image [user] is your Docker hub username and [repo] is the repositories name.
4. Now upload the image by entering - 'docker push [user]/[repo]'
5. Now you can login to Docker playground with your Docker account and start a session and begin a new instance/
6. In the instance enter - 'docker run [user]/[repo]' and it should display a similar output to the image above.

## Credits
- Murray Bosworth
- https://www.hyperiondev.com/ for their course resources
