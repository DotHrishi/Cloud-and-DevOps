import pymysql

DB_HOST = 'notes-db.c4j8kemku47n.us-east-1.rds.amazonaws.com'
DB_USER = 'admin'
DB_PASSWORD = 'hrishi123'
DB_NAME = 'notes_app'
DB_PORT = 3306

def connect_db():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

def create_note(title, content):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO notes (title, content) VALUES (%s, %s)"
    cursor.execute(sql, (title, content))
    conn.commit()
    print(f"Note created with ID: {cursor.lastrowid}")
    cursor.close()
    conn.close()

def view_all_notes():
    conn = connect_db()
    cursor = conn.cursor()
    sql = "SELECT id, title, content, created_at FROM notes"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Title: {row[1]}, Content: {row[2]}, Created: {row[3]}")
    cursor.close()
    conn.close()

def view_note(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "SELECT id, title, content, created_at FROM notes WHERE id = %s"
    cursor.execute(sql, (note_id,))
    result = cursor.fetchone()
    if result:
        print(f"ID: {result[0]}, Title: {result[1]}, Content: {result[2]}, Created: {result[3]}")
    else:
        print("Note not found")
    cursor.close()
    conn.close()

def edit_note(note_id, new_title, new_content):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "UPDATE notes SET title = %s, content = %s WHERE id = %s"
    cursor.execute(sql, (new_title, new_content, note_id))
    conn.commit()
    print(f"Note {note_id} updated" if cursor.rowcount > 0 else "Note not found")
    cursor.close()
    conn.close()

def delete_note(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "DELETE FROM notes WHERE id = %s"
    cursor.execute(sql, (note_id,))
    conn.commit()
    print(f"Note {note_id} deleted" if cursor.rowcount > 0 else "Note not found")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_note("Test Note", "This is a test note content.")
    view_all_notes()
    view_note(1)
    edit_note(1, "Updated Test Note", "Updated content.")
    delete_note(1)