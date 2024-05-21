from os.path import abspath, join, exists, dirname, isdir, basename
from os import walk, getcwd
from file_handler import FileHandler
from pydantic import BaseModel

class SaveFolderArgs(BaseModel):
    folder_path:str

class MocksHandler:
    def __init__(self, project_folder_path:str = None):
        self.project_folder_path = project_folder_path
        if self.project_folder_path is None:
            self.project_folder_path = getcwd()
        else:
            if not exists(self.project_folder_path):
                raise ValueError(f'project_folder_path {project_folder_path} does not exists!')                
        self.project_folder_path = abspath(self.project_folder_path)
        self.mocks_folder = None

    def get_mocks_folder(self) -> str:
        for root, dirs, files in walk(self.project_folder_path):
            if 'mocks' in dirs and 'build' not in root:
                self.mocks_folder = abspath(join(root, 'mocks'))
                return self.mocks_folder
        raise ValueError(f'No mocks folder found in {self.project_folder_path}')

    def get_filepath(self, filename_with_extension:str, is_dumping:bool = False):
        self.get_mocks_folder()
        filepath = join(self.mocks_folder, filename_with_extension)
        if not exists(filepath) and not is_dumping:
            raise ValueError(f'File {filepath} not found')
        return filepath

    def dump_in_mocks_folder(self, filename:str, data:dict, extension:str = 'json'):
        filepath = self.get_filepath(f'{filename}.{extension}', is_dumping = True)
        FileHandler.write(file_handler_data={filepath: data})

    def load_from_mocks_folder(self, filename:str, extension:str = 'json', mode:str = 'r'):
        filepath = self.get_filepath(f'{filename}.{extension}')
        return FileHandler.load(file_paths=filepath, load_first_value=True, mode=mode)