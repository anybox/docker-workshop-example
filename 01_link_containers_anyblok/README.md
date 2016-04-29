# Link container

This example intents to demonstrate how to link 2 docker containers.
A DBMS Docker container using [PostgreSQL image](
https://hub.docker.com/_/postgres/ "Postgres on docker hub") and an homemade
container which is a todo REST API that uses http verbes based on [Anyblok](
http://docs.anybox.fr/anyblok/default/) to manage todo list on server side

## Start postgresql Docker container

```bash
$ docker run -d --name pganyblok \
    -e POSTGRES_PASSWORD=pgpass \
    -e POSTGRES_USER=pguser \
    postgres
```

## Build todo service Docker container

```bash
$ docker build -t 01_todo_service .
```


## Initialize an instance (BD)

```bash
$ docker run --rm -it --link pganyblok:database 01_todo_service \
        anyblok_createdb --install-bloks todo todo_service -c anyblok.cfg
```

## Start the server

```bash
$ docker run --rm -it -p 0.0.0.0:8082:8080 --link pganyblok:database 01_todo_service
```


## API Documentation

### GET the todo list

```bash
$ curl localhost:8080/todo
```


### GET a specific todo

```bash
$ curl localhost:8080/todo/2
```


### PUT a new todo

```bash
$ curl -X PUT \
       -H "Content-Type: application/json" \
       -d '{"task": "An other thing todo"}' \
       localhost:8080/todo
```

### DELETE a specific todo

```bash
$ curl -X DELETE localhost:8080/todo/2
```

### PATCH a specific todo


```bash
$ curl -X PATCH \
       -H "Content-Type: application/json" \
       -d '{"task": "Fix task label and change state", "done": true}' \
       localhost:8080/todo/2
```

