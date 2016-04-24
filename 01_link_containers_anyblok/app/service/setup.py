from setuptools import setup

bloks = [
    'todo_service=todo_service:TodoServiceBlok',
],

requires = [
    'anyblok_pyramid',
    'business'
]

setup(
    name='service',
    version='0.0.1',
    description='Services',
    author='Pierre Verkest',
    author_email='pverkest@anybox.fr',
    url='https://github.com/petrus-v/docker-workshop-example',
    packages=[
        'todo_service',
    ],
    install_requires=requires,
    license='AGPL-3.0',
    entry_points={
        'bloks': bloks,
    },
)
