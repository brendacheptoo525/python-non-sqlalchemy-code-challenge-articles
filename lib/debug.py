class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name



class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if not isinstance(category, str):
            raise TypeError("Category must be of type str")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class")
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title
