import json
import datetime

class Note:
    def __init__(self, id, title, body, created):
        self.id = id
        self.title = title
        self.body = body
        self.created = created
        self.edited = created


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

while True:
    print("1. Add note")
    print("2. Edit note")
    print("3. Delete note")
    print("4. Print notes")
    print("5. Save notes")
    print("6. Load notes")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter note title: ")
        body = input("Enter note body: ")
        app.add_note(title, body)
    elif choice == "2":
        id = int(input("Enter note ID: "))
        new_title = input("Enter new note title: ")
        new_body = input("Enter new note body: ")
        app.edit_note(id, new_title, new_body)
    elif choice == "3":
        id = int(input("Enter note ID: "))
        app.delete_note(id)
    elif choice == "4":
        app.print_notes()
    elif choice == "5":
        filename = input("Enter filename to save notes: ")
        app.save_notes(filename)
    elif choice == "6":
        filename = input("Enter filename to load notes: ")
        app.load_notes(filename)
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
