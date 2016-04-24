from anyblok.blok import Blok


class TodoBlok(Blok):

    version = '1.0.0'

    def install(self):
        """ method called at blok installation time """
        self.registry.Todo.multi_insert(
            {'task': "Cook vegetables"},
            {'task': "Wash sofa"},
            {'task': "Change car wheels", 'done': True},
        )

    def update(self, latest_version):
        if latest_version is None:
            self.install()

    @classmethod
    def import_declaration_module(cls):
        from . import todo  # noqa