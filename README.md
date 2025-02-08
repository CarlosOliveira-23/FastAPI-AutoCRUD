# 🚀 Automatic REST API Generator

## 📌 Project Overview
This project is an **Automatic REST API Generator** built with **FastAPI** and **SQLAlchemy**. It reads a **PostgreSQL/MySQL** database and generates a fully functional **CRUD API** automatically.

## 📜 Features
- 🏗️ **Automatic API Generation** from a Database
- 🔥 **FastAPI** for high-performance backend
- 🛠️ **SQLAlchemy** for ORM and database interaction
- 🐳 **Docker & Docker Compose** for containerized deployment
- 🛡️ **Environment Variable Management** using `.env`
- 🔍 **Swagger UI** for API Documentation (`/docs`)

## 🏗️ Project Structure
```
├── app/
│   ├── models/        # Database models
│   ├── routes/        # API routes
│   ├── database.py    # Database connection setup
│   ├── main.py        # Main FastAPI app entry point
│
├── .env               # Environment variables (ignored in git)
├── .gitignore         # Ignore unnecessary files
├── Dockerfile         # Docker build configuration
├── docker-compose.yml # Docker Compose setup for API & DB
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
```

## 🔧 Setup & Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/gerador_api_rest.git
cd gerador_api_rest
```

### 2️⃣ Create and Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file with your database credentials:
```ini
DATABASE_URL=postgresql://user:password@localhost:5432/gerador_api_rest
```

### 5️⃣ Initialize the Database
Run the following command to create the tables in the database:
```sh
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

### 6️⃣ Run the Application
```sh
uvicorn app.main:app --reload
```
Now, open your browser and access:
- 🌍 **API Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🐳 Running with Docker
### Build and Run Container
```sh
docker-compose up --build
```

## 📡 API Endpoints
### 🔹 Users
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/users/` | Get all users |
| `POST` | `/users/` | Create a new user |

### 🔹 Products
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/products/` | Get all products |
| `POST` | `/products/` | Create a new product |

## 🚀 Contribution
1. **Fork** the repository.
2. **Create a branch** (`git checkout -b feature-branch`)
3. **Commit changes** (`git commit -m "Added feature"`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Create a Pull Request** 🚀

## 📜 License
This project is **MIT Licensed**. Feel free to use and modify it!

