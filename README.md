
# StreamFlix 🎬

StreamFlix is a full-stack streaming platform inspired by modern streaming services. It aims to give users more control over video quality and data consumption while enjoying their favourite movies.

## Project Goals

The goal of StreamFlix is to explore how streaming technology can provide users with greater transparency and control over their data usage.

## Key Features

- Manual video quality selection.
- Data Saver mode to help reduce data consumption.
- Estimated data usage tracking.
- Movie browsing and discovery.
- User preferences.

## Technology Stack

### Frontend
- React
- TypeScript

### Backend
- Python
- FastAPI

### Database
- PostgreSQL

### Video Streaming
- HLS.js

### Other Tools
- Git
- GitHub
- TMDB API (movie metadata)

## Current Progress

- [x] Python development environment setup.
- [x] FastAPI backend created.
- [x] Movie data model created using Pydantic.
- [x] Movie listing endpoint.
- [x] Movie filtering by genre.
- [x] Retrieve individual movies by ID.
- [x] Initial project pushed to GitHub.
- [ ] PostgreSQL database integration.
- [ ] React frontend development.
- [ ] Video playback integration.
- [ ] Manual video quality selection.
- [ ] Data Saver functionality.

## Running the Backend

1. Clone the repository:

   `git clone https://github.com/Faithtsemi/StreamFlix.git`

2. Navigate into the project:

   `cd StreamFlix`

3. Create a virtual environment:

   `python -m venv venv`

4. Activate the environment in PowerShell:

   `.\venv\Scripts\Activate.ps1`

5. Install dependencies:

   `pip install -r backend/requirements.txt`

6. Navigate to the backend folder:

   `cd backend`

7. Start the development server:

   `python -m uvicorn main:app --reload`

8. Open the API documentation:

   `http://127.0.0.1:8000/docs`

## Project Status

StreamFlix is currently under active development. Features and functionality will be added incrementally.

## Author

Faith Tsemi
