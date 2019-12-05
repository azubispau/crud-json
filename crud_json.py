import json
import os
"""
empty json looks like this: {"person_data": []}
"""
TEST_JSON_FILENAME = 'person_data.json'
person_data_json = os.path.join(os.getcwd(), TEST_JSON_FILENAME)


def read_json(filename=person_data_json):
    """
    returns: json as python dict.
    """
    with open(filename,) as json_file:
        json_data = json.load(json_file)
        return json_data


def write_to_json_file(data, json_array="person_data", filename=person_data_json):
    """
    appends single or multiple person data to json.
    """
    current_data = read_json()
    current_data[json_array].append(data)
    with open(filename, 'w') as f_json:
        json.dump(current_data, f_json)


def delete_from_json_file(val, key="id", json_array="person_data", filename='person_data.json'):

    current_data = read_json()
    filtered_array = [record for record in current_data[json_array] if not (key in record and record[key] == val)]
    if filtered_array != current_data[json_array]:
        current_data[json_array] = filtered_array
        with open(filename, 'w') as f_json:
            json.dump(current_data, f_json)


class Person:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname

    def get_dict_data(self):
        res = {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }
        return res

    def get_json_data(self):
        dict_data = self.get_dict_data()
        json_data = json.dumps(dict_data)
        return json_data

    @staticmethod
    def get_some_text(text):
        return text


class Samurai(Person):

    def __init__(self, id, name, surname, sword_name):
        super().__init__(id, name, surname)
        self.sword_name = sword_name


if __name__ == '__main__':

    json_dict = read_json()

    print(json_dict["person_data"])

#     CREATE
    id = input("Enter id: ")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    asmuo = Person(id, name, surname)
    write_to_json_file(asmuo.get_dict_data())
#
#     READ
#     print(read_json())
#
#     DELETE
#     delete_from_json_file('id', '10')
