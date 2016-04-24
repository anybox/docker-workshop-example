from anyblok.blok import Blok


class TodoServiceBlok(Blok):

    version = '1.0.0'

    @classmethod
    def pyramid_load_config(cls, config):
        config.add_route('todo-list', '/todo', request_method='GET')
        config.add_route('todo-add', '/todo', request_method='PUT')
        config.add_route('todo', '/todo/{id}', request_method='GET')
        config.add_route('todo-delete', '/todo/{id}', request_method='DELETE')
        config.add_route('todo-update', '/todo/{id}', request_method='PATCH')
        config.scan(cls.__module__ + '.services')
