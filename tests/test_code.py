import json
import os
import pytest
from datetime import datetime
from utils.code import load_operations
from utils.code import sort_last_five
from utils.code import date_reform
from utils.code import from_reform
from utils.code import to_reform
from utils.code import execute_sort



def test_load_json():
    data = load_operations()
    assert all(isinstance(item, dict) for item in data), "ошибка синтаксиса данного словаря"


def test_execute_sort():
    "проверяем список сортированный по 'EXECUTED'"
    list_actions = load_operations()
    listing = execute_sort(list_actions)
    if "state" in listing:
        assert "EXECUTED" in listing


def test_sort_last_five():
    data = load_operations()
    elements = sort_last_five(data)
    assert len(elements) == 5, "количество отсортированных элементов должно быть равным 5"


def test_date_reform():
    list_actions = load_operations()
    listing = sort_last_five(list_actions)
    re_date = date_reform(listing)
    first_dict = re_date[0]
    date = first_dict['date']
    date_obj = datetime.strptime(date, '%d.%m.%Y')
    assert date_obj


def test_from_reform():
    list_actions = load_operations()
    listing = sort_last_five(list_actions)
    re_from = from_reform(listing)
    first_dict = re_from[0]
    from_unit = first_dict['from']
    assert "** ****" in from_unit


def test_to_reform():
    list_actions = load_operations()
    listing = sort_last_five(list_actions)
    re_to = to_reform(listing)
    first_dict = re_to[0]
    to_unit = first_dict['to']
    assert "Счет **" in to_unit