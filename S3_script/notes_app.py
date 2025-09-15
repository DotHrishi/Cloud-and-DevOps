import mysql.connector

# AWS RDS connection details
DB_HOST = "notes-db.c4j8kemku47n.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "hrishi123"
DB_NAME = "notes_app"

# Function to connect
def connect_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# Create Note
def add_note(title, content):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
    conn.commit()
    conn.close()
    print(f"✅ Note added: {title}")

# View Notes
def view_notes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()
    conn.close()
    print("\n📜 All Notes:")
    for row in rows:
        print(f"ID: {row[0]}, Title: {row[1]}, Content: {row[2]}")

# Update Note
def update_note(note_id, new_title, new_content):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET title=%s, content=%s WHERE id=%s", (new_title, new_content, note_id))
    conn.commit()
    conn.close()
    print(f"✏️ Note {note_id} updated.")

# Delete Note
def delete_note(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=%s", (note_id,))
    conn.commit()
    conn.close()
    print(f"🗑️ Note {note_id} deleted.")

# Main menu
def menu():
    while True:
        print("\n--- Notes App ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            add_note(title, content)
        elif choice == "2":
            view_notes()
        elif choice == "3":
            note_id = int(input("Note ID to update: "))
            title = input("New Title: ")
            content = input("New Content: ")
            update_note(note_id, title, content)
        elif choice == "4":
            note_id = int(input("Note ID to delete: "))
            delete_note(note_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    menu()
