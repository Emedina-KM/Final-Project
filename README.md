# 1. Create a virtual environment

```shell
python -m venv venv
.\venv\Scripts\activate
```

# 2. Install requirements

```shell
pip install -r requirements.txt
```

# 3. (Optional) Run the application locally for testing without Docker

```shell
python .\app.py
```

# 4. Run docker-compose

```shell
docker compose -p flask-docker-compose up -d
```

# 5. Stop and rebuild docker-compose

```shell
docker compose down
docker compose build --no-cache
docker compose up -d
```

# 6. Install Thunder Client for API testing (VS Code Extension)

```shell
# Open VS Code and go to Extensions (Ctrl+Shift+X), then search for "Thunder Client" and install it.
```

# 7. Test the API using Thunder Client

```shell
# 7.1. Open Thunder Client in VS Code.
# 7.2. Create a new POST request to the following URL: 
#    http://127.0.0.1:8000/churn
# 7.3. In the request body (JSON format), enter the following:
#    {
#      "age": x,
#      "tenure": y
#    }
# 7.4. Click "Send" to test the endpoint.
```

# 6. (Optional) Remove all containers

```shell
docker compose down
```