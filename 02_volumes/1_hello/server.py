import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from atomicfile import AtomicFile

COUNTER_PATH = os.getenv('COUNTER_PATH', '/tmp/counter.txt')


def hello_world(request):
    add_visit()
    return Response('Hello %(name)s!' % request.matchdict)


def add_visit():
    counter = 0
    try:
        with open(COUNTER_PATH, "r") as f:
            counter = int(f.read())
    except:
        pass

    counter += 1

    with AtomicFile(COUNTER_PATH, "w") as f:
        f.write(str(counter))
        f.close()

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    print("Server started! visit http://localhost:????/hello/{Your name}")
    server.serve_forever()
