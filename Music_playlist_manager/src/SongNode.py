class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

    def __str__(self):
        return self.title