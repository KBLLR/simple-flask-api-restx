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

The API server will start using the PORT `5000`.

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

> **Step #2** - create virtual environment using python3 and activate it (keep it outside our project directory)

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

Copy the example env file and keep the real file local. `.env` and `.env.*` are gitignored; `.env.example` is the template (`SECRET_KEY` empty, `FLASK_ENV=development`).

```bash
$ cp .env.example .env
```

`flask run` loads `.env` when `python-dotenv` is installed. You can also export the variables yourself:

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

When `FLASK_ENV=development` and `SECRET_KEY` is missing, startup generates an ephemeral key and prints a warning. Sessions from that key do not survive a restart. Set `SECRET_KEY` in `.env` (or export it) when you need a stable key. If `FLASK_ENV` is anything else, or is unset, the app exits with an error until `SECRET_KEY` is set.

> Or for Windows-based systems

```powershell
$ copy .env.example .env
$ (Windows CMD) set FLASK_APP=run.py
$ (Windows CMD) set FLASK_ENV=development
$
$ (Powershell) $env:FLASK_APP = ".\run.py"
$ (Powershell) $env:FLASK_ENV = "development"
```

<br />

> **Step #5** - start test APIs server at `localhost:5000`

```bash
$ flask run
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
