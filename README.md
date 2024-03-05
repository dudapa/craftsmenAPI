# Craftsmen REST API

Craftsmen REST API is a Django and Django REST framework-based project designed to provide information about craftsmen, their projects, and reviews from customers. The API supports the creation of craftsman or visitor profiles, each having different privileges. Authentication is implemented using JSON Web Token (JWT) from Django REST framework Simple JWT and Djoser.

## Technologies Used

- Python
- Django
- Django REST framework
- MySQL
- Djoser
- JWT Web Token

## Endpoints

### Craftsmen

- List all and create craftsmen: [http://127.0.0.1:8000/api/v1/craftsmen/](http://127.0.0.1:8000/api/v1/craftsmen/)
- Retrieve, update and delete a specific craftsman: [http://127.0.0.1:8000/api/v1/craftsmen/<pk>/](http://127.0.0.1:8000/api/v1/craftsmen/<pk>/)
- List all and create projects for a craftsman: [http://127.0.0.1:8000/api/v1/craftsmen/<pk>/projects/](http://127.0.0.1:8000/api/v1/craftsmen/<pk>/projects/)
- Retrieve, update and delete a specific project for a craftsman: [http://127.0.0.1:8000/api/v1/craftsmen/<pk>/projects/<pk>/](http://127.0.0.1:8000/api/v1/craftsmen/<pk>/projects/<pk>/)
- List all and create reviews for a craftsman: [http://127.0.0.1:8000/api/v1/craftsmen/<pk>/reviews/](http://127.0.0.1:8000/api/v1/craftsmen/<pk>/reviews/)
- Retrieve, update and delete a specific review for a craftsman: [http://127.0.0.1:8000/api/v1/craftsmen/<pk>/reviews/<pk>/](http://127.0.0.1:8000/api/v1/craftsmen/<pk>/reviews/<pk>/)

### Skills

- List all and create skills: [http://127.0.0.1:8000/api/v1/skills/](http://127.0.0.1:8000/api/v1/skills/)
- Retrieve, update and delete a specific skill: [http://127.0.0.1:8000/api/v1/skills/<pk>/](http://127.0.0.1:8000/api/v1/skills/<pk>/)

### Visitors

- List all and create visitors: [http://127.0.0.1:8000/api/v1/visitors/](http://127.0.0.1:8000/api/v1/visitors/)
- Retrieve, update and delete a specific visitor: [http://127.0.0.1:8000/api/v1/visitors/<pk>/](http://127.0.0.1:8000/api/v1/visitors/<pk>/)

### Djoser Authentication

- List all and create users: [http://127.0.0.1:8000/auth/users/](http://127.0.0.1:8000/auth/users/)
- Retrieve, update and delete the authenticated user: [http://127.0.0.1:8000/auth/users/me/](http://127.0.0.1:8000/auth/users/me/)

### JWT Web Token

- Create a JWT token: [http://127.0.0.1:8000/auth/jwt/create/](http://127.0.0.1:8000/auth/jwt/create/)
- Refresh a JWT token: [http://127.0.0.1:8000/auth/jwt/refresh/](http://127.0.0.1:8000/auth/jwt/refresh/)

## Usage

### Prerequisites

Make sure you have [Python](https://www.python.org/) and [pipenv](https://pipenv.pypa.io/en/latest/) installed on your system.

### Installation

1. Clone the repository:
   git clone https://github.com/your-username/craftsmen-rest-api.git
   cd craftsmen-rest-api

2. Install dependencies using pipenv:
   pipenv install

3. Activate the virtual:
   pipenv shell

4. Apply database migrations:
   python manage.py migrate

5. Run development server
   python manage.py runserver


## License

This project is licensed under the MIT License.


## Contact

- Email: patrikduda001@gmail.com
