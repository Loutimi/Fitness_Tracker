Fitness Tracker API
The Fitness Tracker API is a web-based API built with Django and Django Rest Framework (DRF) that allows users to log, track, and manage their fitness activities. The API also includes user authentication, calorie tracking, and a leaderboard feature to help users track their progress compared to others. This project was designed to promote healthy living by encouraging users to monitor their fitness routines.
Features
User Authentication: Sign up, log in, and access the API securely using JSON Web Tokens (JWT).
Activity Logging: Log various fitness activities with relevant metrics like calories burned, distance, and duration.
Leaderboard: View user rankings based on total calories burned and number of activities.
CRUD Operations: Create, read, update, and delete activities.
Pagination and Filtering: Retrieve paginated and filterable activity logs.
Data Validation: Ensure proper validation for activity data (e.g., allowing null for distance if it's a weightlifting activity).
API Endpoints
Authentication
POST /api/auth/register/ — Register a new user.
POST /api/auth/login/ — Log in and retrieve a JWT token.
User Activities
GET /api/activities/ — List all logged activities (supports filtering and pagination).
POST /api/activities/ — Create a new fitness activity.
GET /api/activities/{id}/ — Retrieve a specific activity.
PUT /api/activities/{id}/ — Update an existing activity.
DELETE /api/activities/{id}/ — Delete a specific activity.
Leaderboard
GET /api/leaderboard/ — View the leaderboard, showing user rankings by total calories burned and number of activities logged.
