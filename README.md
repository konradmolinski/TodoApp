Trying out Vue.js framework on a simple case of todo app.
Simple CRUD operations so far.


# Install

`make install`

# Run dev

Modify .env files:
- `.env` - comment 2 line, uncomment 4
- `frontend.env` - set url to `"http://localhost:8000/"`

Activate environment:
`pipenv shell`

Run database:

`docker-compose start db`

Run frontend:
`make serve_frontend`

Run backend:
`make serve_backend`

Run migrations:

`seed_data_postgres`
