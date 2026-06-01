# Todo List Application

A simple todo list application built with Java Spring Boot backend and React frontend.

## Project Structure

```
.
├── todo-backend/       # Spring Boot REST API
└── todo-frontend/      # React web application
```

## Backend Setup

### Prerequisites
- Java 17 or higher
- Maven 3.6 or higher

### Running the Backend

1. Navigate to the backend directory:
```bash
cd todo-backend
```

2. Build the project:
```bash
mvn clean install
```

3. Run the application:
```bash
mvn spring-boot:run
```

The backend will start on `http://localhost:8080`

### API Endpoints

- `GET /api/todos` - Get all todos
- `GET /api/todos/{id}` - Get a specific todo
- `GET /api/todos/status/{completed}` - Get todos by completion status
- `POST /api/todos` - Create a new todo
- `PUT /api/todos/{id}` - Update a todo
- `DELETE /api/todos/{id}` - Delete a todo
- `DELETE /api/todos` - Delete all todos

### H2 Database Console

Access the H2 console at: `http://localhost:8080/h2-console`

## Frontend Setup

### Prerequisites
- Node.js 14 or higher
- npm or yarn

### Running the Frontend

1. Navigate to the frontend directory:
```bash
cd todo-frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will open automatically at `http://localhost:3000`

## Features

✅ **Create Todos** - Add new todos with title and description
✅ **Mark Complete** - Check off todos as you complete them
✅ **Delete Todos** - Remove todos from your list
✅ **Progress Tracking** - See your completion progress
✅ **Responsive Design** - Works on desktop and mobile devices
✅ **Real-time Sync** - Instant updates between browser and server

## Technology Stack

### Backend
- Spring Boot 3.2.0
- Spring Data JPA
- H2 Database (in-memory)
- Maven

### Frontend
- React 18
- Axios (HTTP client)
- CSS3 (Modern styling)

## CORS Configuration

The backend is configured to accept requests from `http://localhost:3000` (the default React development server). If you need to change this, update the CORS configuration in `TodoApplication.java`.

## Notes

- The H2 database is in-memory, so data will be lost when the server stops
- For production use, replace H2 with a persistent database like PostgreSQL or MySQL
- The frontend uses Axios for API calls
- Both applications use hot-reload during development

## Troubleshooting

**Port already in use:**
- Backend (8080): `lsof -ti:8080 | xargs kill`
- Frontend (3000): `lsof -ti:3000 | xargs kill`

**CORS errors:**
- Make sure both apps are running on the correct ports
- Check the CORS configuration in `TodoApplication.java`

**Dependencies not installing:**
- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` and `package-lock.json`, then run `npm install` again
