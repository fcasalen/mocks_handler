from os import remove, makedirs, removedirs
from os.path import dirname, join, exists
from pytest import raises, fixture
from .handler import MocksHandler

mh = MocksHandler(project_folder_path=dirname(dirname(__file__)))
mocks_folder = join(mh.project_folder_path, 'mocks_handler', 'mocks')
    
def test_get_mocks_folder():
    if exists(mocks_folder):
        removedirs(mocks_folder)
    with raises(ValueError) as e:
        mh.get_mocks_folder()
    assert 'No mocks folder found in' in str(e.value)
    makedirs(mocks_folder)
    assert mh.project_folder_path == dirname(dirname(__file__))
    assert mh.get_mocks_folder() == join(mh.project_folder_path, 'mocks_handler', 'mocks')

def test_get_filepath():
    bad_filename = 'mocks_asdfasdf.txt'
    with raises(ValueError) as exc_info:
        mh.get_filepath(bad_filename)
    filepath = join(mh.get_mocks_folder(), bad_filename)
    assert str(exc_info.value) == f'File {filepath} not found'
    assert filepath == mh.get_filepath(bad_filename, True)

def test_dump_json_in_mocks():
    data = {'a': 2}
    filename = 'mocks_dump'
    mh.dump_in_mocks_folder(filename=filename, data=data)
    assert mh.load_from_mocks_folder(filename=filename) == {'a': 2}
    filepath = join(mh.get_mocks_folder(), f'{filename}.json')
    remove(filepath)
    data = "ola"
    filename = 'mocks_dump_1'
    mh.dump_in_mocks_folder(filename=filename, data=data, extension='txt')
    assert mh.load_from_mocks_folder(filename=filename, extension='txt') == 'ola'
    filepath = join(mh.get_mocks_folder(), f'{filename}.txt')
    remove(filepath)
    removedirs(mocks_folder)