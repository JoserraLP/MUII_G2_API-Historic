import datetime

import six
import typing

 # --------- JSON MANAGER --------- #

import json
from openapi_server.static.constants import DATA_URL

# function to add to JSON 
def append_to_json(data, filename=DATA_URL): 
    try:
        with open(filename) as json_file: 
            file_data = json.load(json_file) 
        
        historic = file_data['historic'] 
    
        data ['id'] = len(historic)

        # appending data to historic  
        historic.append(data) 

        with open(filename,'w') as json_file: 
            json.dump(file_data, json_file, indent=4)

        return True
    except Exception as e:
        print(e)
        return False

# function to read from JSON 
def return_all_json_data(filename=DATA_URL): 
    try:
        with open(filename) as json_file: 
            file_data = json.load(json_file) 
        return file_data
    except Exception as e:
        print(e)
        return None

# function to read from JSON 
def return_json_data(id, filename=DATA_URL): 
    try:
        with open(filename) as json_file: 
            file_data = json.load(json_file) 

        return list(filter(lambda x:x["id"]==id,file_data['historic']))
    except Exception as e:
        print(e)
        return None

 # --------- END JSON MANAGER --------- #

def _deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in six.integer_types or klass in (float, str, bool):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == datetime.date:
        return deserialize_date(data)
    elif klass == datetime.datetime:
        return deserialize_datetime(data)
    elif hasattr(klass, '__origin__'):
        if klass.__origin__ == typing.List:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__origin__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    else:
        return deserialize_model(data, klass)


def _deserialize_primitive(data, klass):
    """Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = six.u(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """Return an original value.

    :return: object.
    """
    return value


def deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :type string: str
    :return: date.
    :rtype: date
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: model object.
    """
    instance = klass()

    if not instance.openapi_types:
        return data

    for attr, attr_type in six.iteritems(instance.openapi_types):
        if data is not None \
                and instance.attribute_map[attr] in data \
                and isinstance(data, (typing.List, dict)):
            value = data[instance.attribute_map[attr]]
            print(value)
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]


def _deserialize_dict(data, boxed_type):
    """Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in six.iteritems(data)}
