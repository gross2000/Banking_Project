import pytest
from datetime import datetime
from utils.code import load_operations
from utils.code import sort_last_five
from utils.code import date_reform
from utils.code import from_reform
from utils.code import to_reform


def test_load_json():
    data = load_operations()
    assert isinstance(data, dict)
    assert 'operation1' in data
    assert 'operation2' in data


def test_date_reform():
    input_data = [
        {"date": "2022-01-30T15:10:00.000"},
        {"date": "2023-02-17T08:45:00.000"}
    ]
    expected_output = [
        {"date": "30.01.2022"},
        {"date": "17.02.2023"}
    ]
    assert date_reform(input_data) == expected_output
    assert date_reform([]) == []
    input_data_missing_date = [
        {"date": "2022-01-30T15:10:00.000"},
        {}
    ]
    expected_output_missing_date = [
        {"date": "30.01.2022"},
        {}
    ]
    assert date_reform(input_data_missing_date) == expected_output_missing_date





