# Churn Prediction API

This API, built with Flask, predicts the likelihood of a customer churning based on two numerical features: **age** and **tenure**. It uses a pre-trained logistic regression model along with a StandardScaler to properly transform the input data. The model and scaler were serialized and loaded at runtime to ensure smooth predictions.

The main endpoint, `/churn`, accepts a POST request with a JSON payload containing `"age"` and `"tenure"`. Input validations ensure that:  
- Both values are positive numbers.  
- The value of `"tenure"` does not exceed `"age"`, which would be illogical in this context.

This solution is based on the **Bank Customer Churn Dataset** available on Kaggle ([https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset)), and has been dockerized for ease of deployment and scalability.

---

## 1. Create a Virtual Environment

```shell
python -m venv venv
.\venv\Scripts\activate
```

## 2. Install requirements

```shell
pip install -r requirements.txt
```

## 3. (Optional) Run the application locally for testing without Docker

```shell
python .\app.py
```

## 4. Run docker-compose

```shell
docker compose -p flask-docker-compose up -d
```

## 5. Stop and rebuild docker-compose

```shell
docker compose down
docker compose build --no-cache
docker compose up -d
```

## 6. Install Thunder Client for API testing (VS Code Extension)

```shell
# Open VS Code and go to Extensions (Ctrl+Shift+X), then search for "Thunder Client" and install it.
```

## 7. Test the API using Thunder Client

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

## 8. (Optional) Remove all containers

```shell
docker compose down
```