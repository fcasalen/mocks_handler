from os.path import abspath, join, exists, dirname, isdir
from os import walk, getcwd
from file_handler import FileHandler
from pydantic import BaseModel

PROJECTS_FOLDER = join(dirname(__file__), 'projects_folder.txt')

class SaveFolderArgs(BaseModel):
    folder_path:str

class MocksHandler:
    def __init__(self, project_name:str, projects_folder_path:str = None):
        if not projects_folder_path:
            if exists(PROJECTS_FOLDER):
                self.projects_folder_path = projects_folder_path
            else:
                self.projects_folder_path = getcwd()
        else:
            if not exists(projects_folder_path):
                raise ValueError(f'projects_folder_path {projects_folder_path} does not exists!')
            self.projects_folder_path = projects_folder_path
        self.project_path = f'{projects_folder_path}/{project_name}'

    def save_projects_folder_path(self, projects_folder_path:str):
        SaveFolderArgs(folder_path=projects_folder_path)
        if not exists(projects_folder_path):
            raise ValueError(f"projects_folder_path {projects_folder_path} doesn't exist!")
        if not isdir(projects_folder_path):
            raise ValueError(f'projects_folder_path {projects_folder_path} is not a directory.')
        with open(PROJECTS_FOLDER, 'w', encoding='utf-8') as f:
            f.write(projects_folder_path)
        print(f'New folder set: {projects_folder_path}!')

    def get_mocks_folder(self) -> str:
        for root, dirs, files in walk(self.project_path):
            if 'mocks' in dirs and 'build' not in root:
                return abspath(join(root, 'mocks'))
        return self.project_path

    def get_filepath(self, filename_with_extension:str, is_dumping:bool = False):
        filepath = f'{self.get_mocks_folder()}/{filename_with_extension}'
        if not exists(filepath) and not is_dumping:
            raise ValueError(f'File {filepath} not found')
        return filepath

    def dump_in_mocks_folder(self, filename:str, data:dict, extension:str = 'json'):
        filepath = self.get_filepath(f'{filename}.{extension}', is_dumping = True)
        FileHandler.write(file_handler_data={filepath: data})

    def load_from_mocks_folder(self, filename:str, extension:str = 'json'):
        filepath = self.get_filepath(f'{filename}.{extension}')
        return FileHandler.load(file_paths=filepath, load_first_value=True)