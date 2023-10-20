import pytest
import User

def temp_user_db(tmp_path):
    user_db = {
        1: ("User1", 1),
        2: ("User2", 3),
        3: ("User3", 5),
    }
    temp_db_path = tmp_path / "temp_user_db.json"
    save_json(temp_db_path, user_db)
    return temp_db_path

def test_invalid_name_user_creation():
    with pytest.raises(ValueError, match="Имя должно быть текстового вида"):
        User(123, 1, 3)

def test_invalid_id_user_creation():
    with pytest.raises(ValueError, match="Личный идентификатор должен быть целым числом"):
        User("InvalidIDUser", "not_an_int", 3)

def test_invalid_level_user_creation():
    with pytest.raises(ValueError, match="Уровень доступа должен быть целым числом от 1 до 7"):
        User("InvalidLevelUser", 1, 8)

def test_valid_user_creation():
    user = User("ValidUser", 1, 3)
    assert user.name == "ValidUser"
    assert user.the_id == 1
    assert user.level == 3

def test_load_json_existing_file(user_db):
    data = load_json(user_db)
    assert isinstance(data, dict)
    assert len(data) == 3

def test_load_json_non_existing_file(path):
    non_existing_file = path / "non_existing.json"
    data = load_json(non_existing_file)
    assert data == {}
