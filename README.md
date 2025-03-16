# flask-auth-testing-kit
Flask Auth Testing Kit is a ready-to-use authentication API built with Flask, designed for developers and testers who want to automate API authentication workflows. It provides a simple implementation of JWT authentication, PKCE (Proof Key for Code Exchange), and token management, making it ideal for learning, testing, and automation.


# Flask Authentication API

This project is a Flask-based authentication API that implements **JWT-based authentication** and **PKCE (Proof Key for Code Exchange)**. It includes:
- User authentication with username and password.
- JWT token generation and verification.
- User logout and token revocation.
- Running the app locally using a virtual environment.
- Running the app using Docker and Docker Compose.

## Features
- **JWT Authentication** using `flask_jwt_extended`
- **User Management** with hashed passwords
- **PKCE (Proof Key for Code Exchange)**
- **Token Revocation** for secure logout
- **Docker & Docker Compose** for easy deployment

---

## 🛠 Installation and Setup

### Prerequisites
- Python 3.8+
- Flask
- PostgreSQL
- Docker & Docker Compose

### 1️⃣ Run Locally using Virtual Environment

#### **Step 1: Clone the Repository**
```sh
$ git clone git@github.com:anandhuk/flask-auth-testing-kit.git
$ cd flask-auth-testing-kit
```

#### **Step 2: Create a Virtual Environment**
```sh
$ python3 -m venv venv
$ source venv/bin/activate  # For Linux/macOS
$ venv\Scripts\activate  # For Windows
```

#### **Step 3: Install Dependencies**
```sh
$ pip install -r requirements.txt
```

#### **Step 4: Set Up Environment Variables**
Update the `.env` file in the project root 

#### **Step 5: Initialize Database**
```sh
$  python setup_db.py
```

#### **Step 6: Run the Flask Application**
```sh
$ python run.py
```
API will be available at `http://127.0.0.1:5000`

---

### 2️⃣ Run using Docker

#### **Step 1: Build the Docker Image**
```sh
$ docker build -t flask-auth-api .
```

#### **Step 2: Run the Container**
```sh
$ docker run -p 5000:5000 flask-auth-api
```

API will be available at `http://127.0.0.1:5000`

---

### 3️⃣ Run using Docker Compose

#### **Step 1: Run Docker Compose**
```sh
$ docker-compose up --build
```
API will be available at `http://127.0.0.1:5000`

---

## 📌 API Endpoints
| Method | Endpoint | Description |
|--------|------------|-------------|
| **GET** | `/authorize` | PKCE-based authentication |
| **POST** | `/token` | Obtain JWT tokens (access & refresh) |
| **GET** | `/user` | Fetch user details (JWT required) |
| **POST** | `/logout` | Revoke access token |

---

## ✅ To-Do List
- [ ] Add user registration endpoint
- [ ] Implement role-based access control (RBAC)
- [ ] Add OAuth2 authentication support
- [ ] Improve logging and error handling
- [ ] Create front-end UI for authentication

---

## 📜 License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## 🤝 Contributing
Pull requests are welcome! If you find any issues, please open an issue or submit a PR.

---

## 📞 Contact
For any questions or support, contact **Anandhu Krishnan G** at **testanandhu@gmail.com**.

Happy coding! 🚀

