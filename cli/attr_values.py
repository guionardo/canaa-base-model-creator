"""
Functions to get default and fake values for model
"""

import faker
import random
from datetime import datetime, date, time
import faker

_promax_default_type_value = {
    int: 0,
    float: 0.0,
    str: "",
    bool: False,
    date: "1970-01-01",
    datetime: "1970-01-01 00:00:00",
    time: "000000"
}

_ms_default_type_value = {
    int: 0,
    float: 0.0,
    str: "",
    bool: False,
    date: datetime(1970, 1, 1),
    datetime: datetime(1970, 1, 1),
    time: 0
}


def get_default_value(data_type, promax: bool):
    _default_type_value = _promax_default_type_value if promax else _ms_default_type_value
    if data_type in _default_type_value:
        return _default_type_value[data_type]
    # TODO: Se for um tipo não primitivo, localizar no cache


def get_fake_value(data_type,promax:bool):
    if data_type == int:
        return random.randint(0, 100)
    elif data_type == float:
        return random.randint(0, 10000)/7
    elif data_type == str:
        fake = faker.Faker()
        return fake.text()
    elif data_type == bool:
        return bool(random.randint(0, 1))
    elif data_type == datetime and promax:
        return 
        return fake.date_time()
    elif data_type == time:
        return fake.time()
    # elif data_type ==date:
    #     return fake. # TODO: Continuar desenvolviment de attr_values
