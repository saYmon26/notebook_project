
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
