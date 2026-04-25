def test_addition():
    assert 2 + 2 == 4


def test_string_upper():
    assert "python".upper() == "PYTHON"


def test_list_append():
    items = [1, 2]
    items.append(3)
    assert items == [1, 2, 3]


def test_dict_lookup():
    data = {"name": "pytest", "version": 8}
    assert data["name"] == "pytest"


def test_any_returns_true():
    assert any([False, False, True]) is True
