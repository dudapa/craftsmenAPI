# Craftsmen REST API

Craftsmen REST API is a Django and Django REST framework-based project designed to provide information about craftsmen, their projects, and reviews from customers. The API supports the creation of craftsman or visitor profiles, each having different privileges. Authentication is implemented using JSON Web Token (JWT) from Django REST framework Simple JWT and Djoser.

## Technologies Used

- Python
- Django
- Django REST framework
- MySQL
- Djoser
- JWT Web Token

## Usage

### Prerequisites

Make sure you have [Python](https://www.python.org/) and [pipenv](https://pipenv.pypa.io/en/latest/) installed on your system.

### Installation

1. Clone the repository:__
   git clone https://github.com/your-username/craftsmen-rest-api.git__
   cd craftsmen-rest-api

2. Install dependencies using pipenv:__
   pipenv install

3. Activate the virtual:__
   pipenv shell

4. Apply database migrations:__
   python manage.py migrate

5. Run development server:
   python manage.py runserver


## License

This project is licensed under the MIT License.


## Contact

- Email: patrikduda001@gmail.com
