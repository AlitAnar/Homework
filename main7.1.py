import os

ROOT = os.path.dirname(__file__)
project_name = 'my_project1'
path = [os.path.join(project_name, 'settings'),
        os.path.join(project_name, 'mainapp'),
        os.path.join(project_name, 'adminapp'),
        os.path.join(project_name, 'authapp')]
for _path in path:
        os.makedirs(os.path.join(ROOT, _path), exist_ok=True)