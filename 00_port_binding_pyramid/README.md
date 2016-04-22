# Port binding


This is the simplest [pyramid](http://pyramid.readthedocs.org
"Pyramid documentation") example in a docker.


Build the image from `Dockerfile`:

```bash
cd path_to/docker-workshop-example/00_port_binding_pyramid
docker build -t 00_pyramid .
```

Run container

```bash
docker run -it --rm -p 0.0.0.0:9080:8080 00_pyramid
```

Then visit ``http://localhost:9080/hello/{Your Name}``

Well done!
