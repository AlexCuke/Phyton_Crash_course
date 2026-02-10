from city_function import get_formatted_city
def test_city_country():
    """Поддерживаются ли имена типа 'Janis Joplin'?"""
    formatted_name = get_formatted_city('Santiago', 'Chilie')
    assert formatted_name == 'Santiago Chilie'
def test_city_country_population():
    """Поддерживаются ли имена типа 'Janis Joplin'?"""
    formatted_name = get_formatted_city('Santiago', 'Chilie', '1000000')
    assert formatted_name == 'Santiago Chilie 1000000'
    
