# Python Flask REST Microservice

REST API written in Python Flask

## Pre-requisites
  - Download & install [Python 3.6](https://www.python.org/downloads/)
  - Download & install [Pipenv](https://docs.pipenv.org/)
   ```bash
    python -m pip install -U pip 
   ```

## Installation

  ```bash
  # Clone the repository 
  git clone {repository name}
  # Change into the directory
  re-direct to cubereum_school_service directory
  # Install all required dependencies with
  pipenv install --deploy --skip-lock
  # Activate the project virtual environment
  pipenv shell

## Running the application

  **Start the app**
  ```bash
  python manage.py run
  ```
## Swagger URL
 http://localhost:8080/

## Usage

**API Specifications**
  - GET: /school
  - GET: /school/filterBy/{field}
  - GET: /school/searchby/address/{value}
  - GET: /school/searchby/area/{value}
  - GET: /school/searchby/field/{field}/value/{value}
  - GET: /school/searchby/landmark/{value}
  - GET: /school/searchby/pincode/{value}
  - GET: /school/searchby/schoolname/{value}
  - GET: /school/sortBy/{field}/forward
 

**Example**
Get all school records
curl http://localhost:808/school
Get some school record by pincode
curl http://localhost:8080/school/searchby/pincode/560062


## Author
Mohan Raj Paramasivam