class Field:
    def __init__(self, name=None, value=None, url=None, status=None):
        self.name = name
        self.value = value
        self.url = url
        self.status = status


class Element:
    def __init__(self):
        self.name = None
        self.type_element = None
        self.fields = None
        self.link_to_image = None
        self.link_to_page_edit = ''
