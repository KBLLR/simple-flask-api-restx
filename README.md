# Flask API Sample

Simple [Flask API Server](https://blog.appseed.us/simple-flask-api-server/) powered by Flask-RestX, SqlAlchemy, **SQLite** persistence - Provided by **AppSeed**. 

<br />

> Features:

- `Up-to-date dependencies` 
- Simple, intuitive codebase - can be extended with ease. 
- `Flask-restX`
- `Docker` support 
- Free [support](https://appseed.us/support) via email and [Discord](https://discord.gg/fZC6hup) (1k+ community).

<br />

## ✨ API Definition

| Route  | Verb | Info | Status | 
|    --- | ---  | --- | --- | 
| `/datas`    | **GET**    | return all items  | ✔️ | 
|             | **POST**   | create a new item | ✔️ |
| `/datas:id` | **GET**    | return one item   | ✔️ | 
|             | **PUT**    | update item       | ✔️ |
|             | **DELETE** | delete item       | ✔️ |

<br />

## ✨ Quick Start in `Docker`

> Get the code

```bash
$ git clone https://github.com/app-generator/flask-api-sample.git
$ cd flask-api-sample
$ cp .env.example .env
```

Set `SECRET_KEY` in `.env` before you start the stack. `.env` is gitignored. With `FLASK_ENV=development` and an empty `SECRET_KEY`, the app generates an ephemeral key for that process. Any other environment stops at startup until `SECRET_KEY` is set.

> Start the app in Docker

```bash
$ docker-compose up --build  
```

The API is published on port `5000` by default. Set `PORT` in `.env` before `docker-compose up` to publish a different host port (macOS AirPlay Receiver already binds `5000`). Nginx inside the stack still listens on container port `5000`.

<br />

![Flask API Server - Open-source Flask Starter provided by AppSeed.](https://user-images.githubusercontent.com/51070104/126349643-264d4cf4-6d0b-4c24-8185-adf69409fa4e.png)

<br />

## ✨ How to use the code

> **Step #1** - Clone the project

```bash
$ git clone https://github.com/app-generator/flask-api-sample.git
$ cd flask-api-sample
```

<br />

> **Step #2** - create virtual environment using Python 3.11+ and activate it (keep it outside our project directory)

SQLAlchemy 2.1 does not install on Python 3.10 or older.

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> **Step #3** - Install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

<br />

> **Step #4** - set environment variables

Copy the example env file and keep the real file local. `.env` and `.env.*` are gitignored; `.env.example` is the template (`SECRET_KEY` empty, `FLASK_ENV=development`, `PORT=5000`).

```bash
$ cp .env.example .env
```

`python run.py` loads `.env` when `python-dotenv` is installed. You can also export the variables yourself:

```bash
$ export FLASK_ENV=development
$ export PORT=5000
```

When `FLASK_ENV=development` and `SECRET_KEY` is missing, startup generates an ephemeral key and prints a warning. Sessions from that key do not survive a restart. Set `SECRET_KEY` in `.env` (or export it) when you need a stable key. If `FLASK_ENV` is anything else, or is unset, the app exits with an error until `SECRET_KEY` is set.

`PORT` is the local dev server port and the Docker host port. It defaults to `5000`. On macOS, AirPlay Receiver occupies `5000`, so set `PORT` to a free port (for example `5001`) when the bind fails.

> Or for Windows-based systems

```powershell
$ copy .env.example .env
$ (Windows CMD) set FLASK_ENV=development
$ (Windows CMD) set PORT=5000
$
$ (Powershell) $env:FLASK_ENV = "development"
$ (Powershell) $env:PORT = "5000"
```

<br />

> **Step #5** - start the API server

The process listens on `PORT` (default `5000`). With `PORT=5001` the server is at `localhost:5001`.

```bash
$ python run.py
```

Use the API via `POSTMAN` or Swagger Dashboard.

![Flask API Sample - Swagger Dashboard.](https://user-images.githubusercontent.com/51070104/151857217-ec364df4-cc90-413f-8bbe-a65e45dc8c35.png)

<br />

## ✨ Project Structure

```bash
api-server-flask/
├── api
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes.py
├── .env.example
├── README.md
├── requirements.txt
└── run.py
```
<br />

---
**[Flask API Sample](https://appseed.us/boilerplate-code/flask-api-boilerplate)** - provided by AppSeed [App Generator](https://appseed.us)
