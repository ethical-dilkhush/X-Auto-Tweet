from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        text TEXT,
                        image TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()
    conn.close()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    text = request.form['text']
    image_file = request.files['image']
    image_path = ''
    
    if image_file:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(image_path)
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO entries (text, image) VALUES (?, ?)", (text, image_path))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'text': text, 'image': image_path})

@app.route('/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/modify/<int:entry_id>', methods=['POST'])
def modify_entry(entry_id):
    new_text = request.form['text']
    new_image = request.files.get('image')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    if new_image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], new_image.filename)
        new_image.save(image_path)
        cursor.execute("UPDATE entries SET text = ?, image = ? WHERE id = ?", (new_text, image_path, entry_id))
    else:
        cursor.execute("UPDATE entries SET text = ? WHERE id = ?", (new_text, entry_id))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'new_text': new_text, 'new_image': image_path if new_image else None})

if __name__ == '__main__':
    app.run(debug=True)
