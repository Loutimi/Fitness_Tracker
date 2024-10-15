# Fitness Tracker API

The **Fitness Tracker API** is a web-based API built with **Django** and **Django Rest Framework (DRF)** that allows users to log, track, and manage their fitness activities. The API includes features such as user authentication, calorie tracking, and a leaderboard to help users monitor their fitness progress and compare it with others. This project promotes healthy living by encouraging users to maintain and track their fitness routines.

## Features

- **User Authentication**: Sign up, log in, and access the API securely using JSON Web Tokens (JWT).
- **Activity Logging**: Log various fitness activities with relevant metrics such as calories burned, distance, duration, and date.
- **Leaderboard**: View user rankings based on total calories burned and the number of activities logged.
- **CRUD Operations**: Create, read, update, and delete fitness activities.
- **Pagination and Filtering**: Retrieve paginated and filterable lists of activity logs.
- **Data Validation**: Ensures proper validation for activity data (e.g., allowing null values for distance when the activity type is weightlifting).

## API Endpoints

### Authentication
- `POST /api/auth/register/` — Register a new user.
- `POST /api/auth/login/` — Log in and retrieve a JWT token.

### User Activities
- `GET /api/activities/` — List all logged activities (supports filtering and pagination).
- `POST /api/activities/` — Create a new fitness activity.
- `GET /api/activities/{id}/` — Retrieve a specific activity.
- `PUT /api/activities/{id}/` — Update an existing activity.
- `DELETE /api/activities/{id}/` — Delete a specific activity.

### Leaderboard
- `GET /api/leaderboard/` — View the leaderboard, displaying user rankings by total calories burned and number of activities logged.