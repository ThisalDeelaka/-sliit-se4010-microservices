# Microservices System

This project contains:
- `item-service` (Node.js + Express) on `8081`
- `order-service` (Django REST Framework) on `8082`
- `payment-service` (ASP.NET Core) on `8083`
- `api-gateway` (Spring Cloud Gateway) on `8080`

All services run with Docker Compose, and requests should be tested through the API Gateway on port `8080`.

## Prerequisites
- Docker
- Docker Compose

## Run
From the project root:

```bash
docker-compose build && docker-compose up -d
```

Check containers:

```bash
docker-compose ps
```

To stop:

```bash
docker-compose down
```

## Gateway Routing (Must-Match)
- `http://localhost:8080/items/**` -> `http://item-service:8081`
- `http://localhost:8080/orders/**` -> `http://order-service:8082`
- `http://localhost:8080/payments/**` -> `http://payment-service:8083`

Important: inside Docker, the gateway routes to Docker service names (`item-service`, `order-service`, `payment-service`), not `localhost`.

## API Endpoints (Test via Gateway)

### Item Service
- `GET /items`
- `POST /items`
- `GET /items/{id}`

### Order Service
- `GET /orders`
- `POST /orders`
- `GET /orders/{id}`

### Payment Service
- `GET /payments`
- `POST /payments/process`
- `GET /payments/{id}`

## Sample Request Bodies

### POST `/items`
```json
{ "name": "Headphones" }
```

### POST `/orders`
```json
{ "item": "Laptop", "quantity": 2, "customerId": "C001" }
```

### POST `/payments/process`
```json
{ "orderId": 1, "amount": 1299.99, "method": "CARD" }
```

## Verification Commands (Gateway Only)

### Linux / macOS

```bash
curl http://localhost:8080/items
curl -X POST http://localhost:8080/items -H "Content-Type: application/json" -d '{"name":"Headphones"}'
curl http://localhost:8080/items/1

curl http://localhost:8080/orders
curl -X POST http://localhost:8080/orders -H "Content-Type: application/json" -d '{"item":"Laptop","quantity":2,"customerId":"C001"}'
curl http://localhost:8080/orders/1

curl http://localhost:8080/payments
curl -X POST http://localhost:8080/payments/process -H "Content-Type: application/json" -d '{"orderId":1,"amount":1299.99,"method":"CARD"}'
curl http://localhost:8080/payments/1
```

### Windows PowerShell (Recommended)
Use `curl.exe` (not `curl`) and force IPv4 to avoid localhost IPv6 conflicts.

```powershell
curl.exe --ipv4 http://localhost:8080/items
curl.exe --ipv4 -X POST http://localhost:8080/items -H "Content-Type: application/json" -d '{"name":"Headphones"}'
curl.exe --ipv4 http://localhost:8080/items/1

curl.exe --ipv4 http://localhost:8080/orders
curl.exe --ipv4 -X POST http://localhost:8080/orders -H "Content-Type: application/json" -d '{"item":"Laptop","quantity":2,"customerId":"C001"}'
curl.exe --ipv4 http://localhost:8080/orders/1

curl.exe --ipv4 http://localhost:8080/payments
curl.exe --ipv4 -X POST http://localhost:8080/payments/process -H "Content-Type: application/json" -d '{"orderId":1,"amount":1299.99,"method":"CARD"}'
curl.exe --ipv4 http://localhost:8080/payments/1
```

## Postman Collection
Import:
- `microservices-gateway.postman_collection.json`

Collection base URL variable:
- `baseUrl = http://localhost:8080`

## Notes
- In-memory data only (no external database).
- ID fields are integer auto-increment.
- Success codes: `200` for GET, `201` for POST.
- Missing IDs return `404`.
- No direct service-to-service calls.
