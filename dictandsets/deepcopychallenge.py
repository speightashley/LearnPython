from contents import recipes


def my_deepcopy(d: dict) -> dict:
    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict
