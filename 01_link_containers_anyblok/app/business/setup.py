from setuptools import setup

bloks = [
    'todo=todo:TodoBlok',
],

requires = [
    'anyblok'
]

setup(
    name='business',
    version='0.0.1',
    description='Business model and method',
    author='Pierre Verkest',
    author_email='pverkest@anybox.fr',
    url='https://github.com/anybox/docker-workshop-example',
    packages=[
        'todo',
    ],
    install_requires=requires,
    license='AGPL-3.0',
    entry_points={
        'bloks': bloks,
    },
)
