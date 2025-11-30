def make_car(manufacturer, model, **user_info):
    """Создает словарь, содержащий информацию о пользователе."""
    user_info['manufacturer'] = manufacturer
    user_info['model'] = model
    return user_info