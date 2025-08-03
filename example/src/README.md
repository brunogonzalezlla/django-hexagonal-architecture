
# Example Django Hexagonal API

This is a sample Django project demonstrating a hexagonal (ports and adapters) architecture for building APIs.

## Features
- Hexagonal structure: clear separation between domain, application, infrastructure, and interfaces
- Django REST Framework integration
- Example domain logic and API endpoints

## Getting Started
1. Install dependencies:
   ```bash
   poetry install
   ```
2. Apply migrations:
   ```bash
   make migrate
   ```
3. Run the development server:
   ```bash
   make start
   ```

## Project Structure
```
src/
├── apps/           # Domain and business logic
├── config/         # Django settings and configuration
├── manage.py       # Django entrypoint
└── db.sqlite3      # Example database
```

## API Example

This project exposes a simple Notes API under the `/notes/` path. You can test the endpoints using tools like curl, httpie, or Postman.

### Available Endpoints

- **List all notes**
  - `GET /notes/`
  - Returns a list of all notes.

- **Retrieve a note by reference**
  - `GET /notes/{reference}/`
  - Returns the details of a note with the given UUID reference.

- **Create a new note**
  - `POST /notes/`
  - Body: `{ "title": "My Note", "content": "Some content" }`
  - Returns the created note.

- **Update an existing note**
  - `PUT /notes/{reference}/`
  - Body: `{ "title": "Updated Title", "content": "Updated content" }`
  - Updates the note with the given reference.

- **Delete a note**
  - `DELETE /notes/{reference}/`
  - Deletes the note with the given reference.

All endpoints return JSON responses. The API uses UUIDs as references for notes.

## License
MIT
