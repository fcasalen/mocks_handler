package to handle mocks folder and its content in your projects, allowing to load and write json (standard) and txt files in it

```python
from mocks_handler import MocksHandler
mh = MocksHandler(project_name='your_project', projects_folder_path='projects_folder')

#if you have a centralized projects folder, you can save it like this and next time you can instantiate MocksHandler without the projects_folder_path argument
mh.save_projects_folder_path(projects_folder_path='your_projects_folder_path')

#writing data to a json in mocks_folder of your project
mh.dump_in_mocks_folder(filename=filename, data=data)

#getting mocks_folder of your project
mh.get_mocks_folder()

#loading data from test.json in mocks_folder of your project
mh.load_from_mocks_folder('test')

#loading data from test.txt in mocks_folder of your project
mh.load_from_mocks_folder('test', extension='txt')

#writing data from test.json in mocks_folder of your project
mh.dump_in_mocks_folder('test', data=your_data)
```
