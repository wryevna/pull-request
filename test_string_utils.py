
import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()

def test_capitalize_simple(utils):
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_already_capitalized(utils):
    assert utils.capitalize("Skypro") == "Skypro"

def test_capitalize_empty_string(utils):
    assert utils.capitalize("") == ""

def test_capitalize_with_numbers(utils):
    assert utils.capitalize("123abc") == "123abc"

def test_capitalize_with_spaces(utils):
    assert utils.capitalize(" hello") == " hello" 

def test_trim_left_spaces(utils):
    assert utils.trim("   skypro") == "skypro"

def test_trim_no_spaces(utils):
    assert utils.trim("skypro") == "skypro"

def test_trim_right_spaces(utils):
    assert utils.trim("skypro   ") == "skypro   " 
def test_trim_only_spaces(utils):
    assert utils.trim("     ") == ""


def test_contains_true_case(utils):
    assert utils.contains("SkyPro", "S") is True

def test_contains_false_case(utils):
    assert utils.contains("SkyPro", "U") is False

def test_contains_multiple_occurrences(utils):
    assert utils.contains("banana", "a") is True

def test_contains_empty_string(utils):
    assert utils.contains("", "a") is False

def test_contains_empty_symbol(utils):
    assert utils.contains("SkyPro", "") is True


def test_delete_single_symbol(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_substring(utils):
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_nonexistent_symbol(utils):
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"

def test_delete_all_characters(utils):
    assert utils.delete_symbol("aaaaa", "a") == ""

def test_delete_empty_symbol(utils):
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"
