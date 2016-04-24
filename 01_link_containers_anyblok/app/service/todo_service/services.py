from pyramid.view import view_config
from anyblok_pyramid import current_blok


@view_config(
    route_name='todo-list',
    installed_blok=current_blok(),
    renderer='json'
)
def todo_list(request):
    registry = request.anyblok.registry
    return [
        {'done': todo.done, 'task': todo.task, 'id': todo.id} for todo in
        registry.Todo.query().all()
    ]


@view_config(
    route_name='todo-add',
    installed_blok=current_blok(),
    renderer='json'
)
def add_todo(request):
    registry = request.anyblok.registry
    task = request.json_body.get('task', '')
    done = request.json_body.get('done', False)
    if not task:
        return "Task should be define"
    registry.Todo.insert(task=task, done=done)


@view_config(
    route_name='todo',
    installed_blok=current_blok(),
    renderer='json'
)
def todo(request):
    registry = request.anyblok.registry
    id = request.matchdict['id']
    if not id.isnumeric():
        return "Id must be an Integer"
    todo = registry.Todo.query().filter_by(
        id=int(request.matchdict['id'])
    ).first()
    if not todo:
        return "id(%s) not found" % request.matchdict['id']
    return {'done': todo.done, 'task': todo.task, 'id': todo.id}


@view_config(
    route_name='todo-delete',
    installed_blok=current_blok(),
    renderer='json'
)
def delete_todo(request):
    registry = request.anyblok.registry
    id = request.matchdict['id']
    if not id.isnumeric():
        return "Id must be an Integer"
    todo = registry.Todo.query().filter_by(
        id=int(request.matchdict['id'])
    ).first()
    if not todo:
        return "id(%s) not found, already deleted?!" % request.matchdict['id']
    todo.delete()


@view_config(
    route_name='todo-update',
    installed_blok=current_blok(),
    renderer='json'
)
def update_todo(request):
    registry = request.anyblok.registry
    id = request.matchdict['id']
    if not id.isnumeric():
        return "Id must be an Integer"
    todo = registry.Todo.query().filter_by(
        id=int(request.matchdict['id'])
    ).first()
    if not todo:
        return "id(%s) not found" % request.matchdict['id']
    task = request.json_body.get('task', todo.task)
    done = request.json_body.get('done', todo.done)
    todo.task = task
    todo.done = done
