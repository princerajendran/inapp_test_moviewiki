# IMDB Dataset Project

## Overview

This project involves creating a web application to search and display information about movies and people from the IMDB dataset. The project includes a Django backend with RESTful APIs and a frontend application for user interaction. The APIs support searching for movies and people with various filters. Authentication is implemented using JWT.

## Project Structure

- `data_handling_script/`: Contains scripts for importing data from IMDB datasets into the database.
- `movies/`: Contains Django app including models, views, and a custom Django management command for user creation.
- `front_end/`: Contains the React JS frontend application for interacting with the APIs.

## Data Sources

- **Person Names**: [name.basics.tsv.gz](https://datasets.imdbws.com/name.basics.tsv.gz)
- **Movie Titles**: [title.basics.tsv.gz](https://datasets.imdbws.com/title.basics.tsv.gz)

## Setup Instructions

### Backend Setup

1. **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Requirements**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**

    ```bash
    python manage.py migrate
    ```

5. **Import Data**

    Place the downloaded TSV files in the `data_handling_script/` directory. Then run the data import script:

    ```bash
    python data_handling_script/import_data.py
    ```

6. **Create Superuser**

    Run the following command to create a Django superuser:

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Server**

    ```bash
    python manage.py runserver
    ```

### Frontend Setup

1. **Navigate to Frontend Directory**

    ```bash
    cd front_end
    ```

2. **Install Node Modules**

    ```bash
    npm install
    ```

3. **Start the Development Server**

    ```bash
    npm start
    ```

## API Endpoints

### Search Movies

- **Endpoint**: `/api/movies/`
- **Method**: GET
- **Parameters**: 
  - `year` (optional)
  - `genre` (optional)
  - `person_name` (optional)
  - `type` (optional, e.g., Movie, TV Series, Documentary)
- **Response**: 
  - `title`
  - `year_released`
  - `type`
  - `genre`
  - `list_of_people_associated`

### Search People

- **Endpoint**: `/api/people/`
- **Method**: GET
- **Parameters**: 
  - `movie_title` (optional)
  - `name` (optional)
  - `profession` (optional)
- **Response**:
  - `name`
  - `birth_year`
  - `profession`
  - `known_for_titles`

## Authentication

- **JWT**: Authentication is handled using JWT. Access tokens are required to access the API endpoints. 

### User Creation

- A custom Django management command is included to create hardcoded users for testing purposes.

    ```bash
    python manage.py create_test_users
    ```

## Testing

- Run Django tests using:

    ```bash
    python manage.py test
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
