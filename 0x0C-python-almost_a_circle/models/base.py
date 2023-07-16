#!/user/bin/python
"""
No Modules Imported
Class Base Module
"""


class Base:
    """
    private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constractor to inistatiation of objs
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
