# Flight Routes System

A simple Django-based web application to manage and analyze flight routes between airports. This system models flight paths as a tree structure, allowing you to calculate routes, durations, and specific node locations.

## Features

This application includes four main features:

1.  **Add Route**:
    *   Add new airports to the network.
    *   Define connections by specifying a "Parent Airport", the direction ("Left" or "Right"), and the flight duration.
    *   Before adding a child node (destination), you must ensure the parent node (origin) exists.
    *   **URL**: `http://127.0.0.1:8000/add/`

2.  **Find Nth Node**:
    *   Find a specific airport located 'N' steps away from a starting airport in a specific direction (all Left or all Right).
    *   Useful for analyzing deeper connections in the route network.
    *   **URL**: `http://127.0.0.1:8000/nth-node/`

3.  **Shortest Route**:
    *   Calculate the most efficient path between *any* two airports in the system.
    *   Displays the total duration and the exact path (e.g., A -> B -> C).
    *   **URL**: `http://127.0.0.1:8000/shortest-route/`

4.  **Longest Route**:
    *   Discover the longest possible flight path starting from a specific airport.
    *   Calculates the maximum duration down all possible branches from the chosen airport.
    *   **URL**: `http://127.0.0.1:8000/longest-route/`

## Prerequisites

*   Python (3.x) installed on your system.
*   Django installed (`pip install django`).

## Installation and Setup

Follow these simple steps to get the project running on your local machine:

1.  **Navigate to the project directory**:
    Open your terminal (Command Prompt or PowerShell) and go to the folder containing `manage.py`.
    ```bash
    cd c:\Users\HP\flight_routes_system
    ```

2.  **Install Django** (if not already installed):
    ```bash
    pip install django
    ```

3.  **Apply Database Migrations**:
    This sets up the database to store your airport routes.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Run the Server**:
    Start the web application.
    ```bash
    python manage.py runserver
    ```

5.  **Access the App**:
    Open your web browser and go to the links mentioned in the "Features" section above (e.g., `http://127.0.0.1:8000/add/`).

## How to Use

*   **Step 1**: Go to the **Add Route** page (`/add/`).
*   **Step 2**: Create a "Root" airport (an airport with no parent) if the system is empty.
*   **Step 3**: Add more airports by selecting an existing airport as the "Parent", choosing a position (Left/Right), and entering the duration.
*   **Step 4**: Use the other pages (Shortest Route, Longest Route, Nth Node) to analyze the network you built.

## Troubleshooting

*   **Error: "One or both airport codes not found"**: Ensure you have typed the airport code exactly as it was added (e.g., "JFK" vs "jfk").
*   **Database errors**: Make sure you ran `python manage.py migrate` before starting the server.
