def get_formatted_name(first, last,middle=''):
    if middle:
        full_name = f"{first} {last} {middle}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

