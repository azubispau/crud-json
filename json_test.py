import json
import os
"""
empty json looks like this: {"test_asmenys": []}
"""
TEST_JSON_FILENAME = 'test.json'
test_json1 = os.path.join(os.getcwd(), TEST_JSON_FILENAME)
test_json = '/home/paulius/PycharmProjects/untitled1/crud-json/test.json'

x = test_json1 == test_json


def read_json(filename=test_json):
    with open(filename,) as json_file:
        json_data = json.load(json_file)
        return json_data


def write_to_json_file(data, filename=test_json):
    current_data = read_json()
    current_data["test_asmenys"].append(data)
    with open(filename, 'w') as test_json:
        json.dump(current_data, test_json)


def delete_from_json_file(id, filename='test.json'):
    pass


class Test:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_dict_data(self):
        res = {
            'name': self.name,
            'surname': self.surname
        }
        return res

    def get_json_data(self):
        dict_data = self.get_dict_data()
        json_data = json.dumps(dict_data)
        return json_data


if __name__ == '__main__':

    vardas = input("Iveskite varda: ")
    pavarde = input("Iveskite varda: ")
    asmuo = Test(vardas, pavarde)
    write_to_json_file(asmuo.get_dict_data())