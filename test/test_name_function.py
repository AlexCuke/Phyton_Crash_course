from name_function import get_formatted_name
def test_first_last_name():
    """Поддерживаются ли имена типа 'Janis Joplin'?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
def test_first_last_middle_name():
    """Поддерживаются ли имена типа 'Wolfgand Amadey Mozart'?"""
    formatted_name = get_formatted_name('Wolfgand', 'Amadey', 'Mozart')
    assert formatted_name == 'Wolfgand Amadey Mozart'