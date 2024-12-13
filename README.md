# Notes API

It is a simple notes API that helps you to manage your notes.

### Tech Stack:
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

### Swagger Docs:
[Swagger Page](http://localhost:8000/docs)

### About the System
This system has two types of users.
1. user
2. admin

**What a user can do?**
- A user can create, view, update, delete tags (only the tags created by themselves)
- A user can create, view, update, delete notes (only the notes created by themselves)
- Multiple tags can be assigned to a note

**What a admin can do?**
- An admin can perform all those operations which a normal user can perform.
- An admin can manage all the users.
- An admin can modify all the notes and tags

