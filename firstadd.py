import json
import datetime

class Note:
    def __init__(self, id, title, body, created):
        self.id = id
        self.title = title
        self.body = body
        self.created = created
        self.edited = created
