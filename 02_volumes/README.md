# Play with volumes


In this example we will use volumes

We are going to re-use [port binding example](
../00_port_binding_pyramid/README.md)

We are going to:

* Count the number of visit to hello service application.
* Create an other docker application that display this number.
* Create a docker application that backup the information to the host machine.

> **Note** Following commands are launch from this ``02_volumes`` directory

## Build and run hello application

```bash
$ docker build -t 02_1_hello -f 1_hello/Dockerfile 1_hello/
$ docker run -d --name hello -p 8080:8080 02_1_hello
$ curl localhost:8080/hello/the_world
$ docker inspect hello
$ sudo cat /var/lib/docker/vfs/dir/7f...dea/counter.txt
```

## Build and run counter application

```bash
$ docker build -t 02_2_counter -f 2_counter/Dockerfile 2_counter/
$ docker run --rm --volumes-from hello -it 02_2_counter
```

If you want you can add an other hello app
```bash
$ docker run -d --name hello2 --volumes-from hello -p 8081:8080 02_1_hello
```

## Build and run backup application

```bash
$ docker build -t 02_3_backup -f 3_backup/Dockerfile 3_backup/
$ docker run 
    --rm -it \
    --volumes-from hello \
    -v ~/tmp/backup/:/backup/ \
    -e COUNTER_PATH=/data/counter.txt \
    02_3_backup -d /backup/counter.back
```


## Bonus: Build and run fake hello application


```bash
$ docker build -t 02_4_fake_hello -f 4_fake_hello/Dockerfile 4_fake_hello/
$ docker run -d -e WAIT=5 -e INCREMENT=5 --volumes-from hello 02_4_fake_hello
$ docker run -d -e WAIT=3 -e INCREMENT=10 --volumes-from hello 02_4_fake_hello
...
```