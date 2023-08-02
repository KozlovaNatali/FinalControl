import csv
from datetime import datetime

def create_note(note_id, title, body):
    note = {'id': note_id, 'title': title, 'body': body, 'timestamp': str(datetime.now())}
    return note

def save_note(note, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([note['id'], note['title'], note['body'], note['timestamp']])

def read_notes(filename):
    notes = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            note = {'id': row[0], 'title': row[1], 'body': row[2], 'timestamp': row[3]}
            notes.append(note)
    return notes

def edit_note(note_id, title, body, filename):
    notes = read_notes(filename)
    for note in notes:
        if note['id'] == note_id:
            note['title'] = title
            note['body'] = body
            note['timestamp'] = str(datetime.now())
            break
    write_notes(notes, filename)

def delete_note(note_id, filename):
    notes = read_notes(filename)
    notes = [note for note in notes if note['id'] != note_id]
    write_notes(notes, filename)

def write_notes(notes, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for note in notes:
            writer.writerow([note['id'], note['title'], note['body'], note['timestamp']])