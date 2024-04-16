from os import remove
from os.path import dirname, join
from pytest import raises, fixture
from .handler import MocksHandler

@fixture
def mh():
    # Inicialize a classe fixture aqui, se necessário
    mh = MocksHandler(project_name='mocks_handler', projects_folder_path=dirname(__file__).replace('mocks_handler/mocks_handler', ''))
    return mh

def test_get_mocks_folder(mh:MocksHandler):
    assert mh.get_mocks_folder() == join(dirname(__file__), 'mocks')

def test_get_filepath(mh:MocksHandler):
    bad_filename = 'mocks_asdfasdf.txt'
    with raises(ValueError) as exc_info:
        mh.get_filepath(bad_filename)
    filepath = join(mh.get_mocks_folder(), bad_filename)
    assert str(exc_info.value) == f'File {filepath} not found'
    assert filepath == mh.get_filepath(bad_filename, True)

def test_dump_json_in_mocks(mh:MocksHandler):
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