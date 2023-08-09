 
class NotesApp:
    def __init__(self):
        self.notes = []

    def add_note(self, title, body):
        id = len(self.notes) + 1
        created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(id, title, body, created)
        self.notes.append(note)

    def edit_note(self, id, new_title, new_body):
        for note in self.notes:
            if note.id == id:
                note.title = new_title
                note.body = new_body
                note.edited = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return

    def delete_note(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                return

    def save_notes(self, filename):
        data = []
        for note in self.notes:
            note_data = {'id': note.id, 'title': note.title, 'body': note.body, 'created': note.created, 'edited': note.edited}
            data.append(note_data)
        
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_notes(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        
        self.notes = []
        for note_data in data:
            note = Note(note_data['id'], note_data['title'], note_data['body'], note_data['created'])
            note.edited = note_data['edited']
            self.notes.append(note)

    def print_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}")
            print(f"Title: {note.title}")
            print(f"Body: {note.body}")
            print(f"Created: {note.created}")
            print(f"Edited: {note.edited}")
            print("----------------------")

app = NotesApp()

