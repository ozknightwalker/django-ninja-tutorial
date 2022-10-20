### Django Ninja Tutorial

This project aims to clone the NBI clearance site using django + django_ninja packages


### Steps to Run the project locally
1. Install `docker` and `docker-compose`
2. run the docker services
```commandline
make run-server
```
3. Run the migrations
```commandline
make migrate
```
4. Now access the site through `localhost:8000` or you can check the docker services and see what's the port of the `web` service
```commandline
make services
```
5. Stop services
```commandline
make stop-server
```