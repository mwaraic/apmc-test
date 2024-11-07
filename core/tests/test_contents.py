from core.contents import Contents
import pandas as pd
import json


def open_file(path: str):

    with open(path, 'r') as file:
        return file.read()


class TestContents:

    obj = Contents(architecture='abc')

    def test_parse(self):
        file = open_file('./core/tests/sample/file.txt')

        data = self.obj.parse(file)

        expected_data = json.loads(open_file('./core/tests/sample/data.json'))

        assert data == expected_data

    def test_transform(self):
        data = json.loads(open_file('./core/tests/sample/data.json'))

        contents = self.obj.transform(data)

        expected_contents = pd.read_json('./core/tests/sample/contents.json')

        for col in ['package_name', 'filename']:
            assert contents[col].to_list() == expected_contents[col].to_list()

    def test_statistics(self):
        contents = pd.read_json('./core/tests/sample/contents.json')

        statistics = self.obj.statistics(contents)

        expected_statistics = open_file('./core/tests/sample/statistics.txt')

        assert statistics == expected_statistics
