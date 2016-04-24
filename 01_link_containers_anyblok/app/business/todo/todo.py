from anyblok import Declarations
from anyblok.column import String, Boolean, Integer

register = Declarations.register
Model = Declarations.Model


@register(Model)
class Todo:

    id = Integer(label="Identifier", primary_key=True)
    task = String(label="Task description")
    done = Boolean(default=False)

    def __str__(self):
        return "%s is %s" % (
            self.task,
            "over. Good job!" if self.done else "waiting for you!"
        )
