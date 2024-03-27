# ecommerce

_This is Advance ecommerce project_

## Goal:

> Minimal Coupling

> High Cohesion (Focus)

I am trying to avoid **Monolith** because it's hard to maintain.

## Features

- RESTfull API
- Token based authentication
- Uploading files
- Sending emails, [Fake SMTP for dev](https://github.com/rnwood/smtp4dev)
- Running background tasks
- Performance testing
- Caching
- Schedule SMS send
- Automated Testing

---

**Dummy data populate from [mockaroo](https://www.mockaroo.com/)**

**Serializing Relationship**

> Primary Key

> String

> Nested Object

> Hyperlink

### \* [To know HTTP STATUS code](https://httpstatuses.io/)

---

Token create

```bashscript
http://127.0.0.1:8000/auth/jwt/create
```

```bashscript
http://127.0.0.1:8000/auth/jwt/refresh
```

#### MOD Hear

```bashscript
JWT refresh token
```

**Dashboard**
![1](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/aa73184b-a196-4ddc-9638-5cfb169720d4)

**Collection**
![2  collection](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/3e2f5528-e2bf-4ce6-874f-c17961f7386a)

- ![3  add collection](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/1ea5c02f-e2b8-4c81-9414-c40db16de4b9)

  **Customer**
  ![4  Customer with membership plan](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/3ffe5380-f758-4706-b0f1-9c88c60a458b)

- Add Customer
  ![5  add customer](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/0d3416c7-81f4-4dee-a0f4-440f29a68e63)

**Orders**
![6  orders](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/b86c158f-3a3a-44e6-9398-3b7b88b88175)

Add Order
![7  add order](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/569a3054-01e7-44f6-8ba5-af5ccfe40734)

**Products**
![8  products](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/a92c4807-3b1f-4d3e-a3c8-01d6bcc15929)

- **Add product**
  ![9  add product](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/c30a4b45-aa3b-4498-9875-f1eb1ed5eb5e)

## Django Rest API

_URL: http://127.0.0.1:8000/store/_
![api home](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/80faf5e4-19ec-44f8-a80b-a60c3f772dd8)

- **Product list**
  _url:http://127.0.0.1:8000/store/products/_
  ![product list](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/2f21db0b-c5e6-4837-adb3-9d53be524fcb)

- **product add**
  ![product add api](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/c133e3d4-f7cd-4c23-9f48-8ddaebf81b26)

- **Product Filtering**
  ![product filtering](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/bd5fc40f-7454-4cbf-9a5c-4e5e67b6b162)

- **Product Details**
  _url:http://127.0.0.1:8000/store/products/423/_
  ![product details](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/07913b1c-ff10-4c78-9451-ce2040974028)

- **Collection list API**
  ![collection list](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/5cc63268-bc0a-4ded-a3d4-4fe27d3383d0)

- **Cart List**
  ![cart list](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/97536a15-0983-48af-9294-9cd9a1e80582)

- **User Create**
  **http://127.0.0.1:8000/auth/users/**
  ![create user](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/4c866355-c075-472f-a5e2-719a1254a99d)

- **Customer List**
  ![customer list](https://github.com/mushfiqur-rahman/ecommerce/assets/26889268/75bf4023-4e7a-40f6-a161-3956f0bcb11a)

---

### Configuring Email Back-end

<b>Type of backend for email:</b>

- SMTP(default)
- Console
- File
- Locmem
- Dummy

### Celery

<b>Long Running tasks:</b>

- Processing Images and videos
- Generating reports
- Sending Emails
- Running machine learning models

### Test Frameworks

- unittest
- pytest
  - More Features
  - Tone of plugins
  - Less boilerplate
    > Tests should have a single responsibility
    > That can be multiple assertion

### Performance Test

```bash
locust -f locustfiles/browse_products.py
```

> Open Browser

```bash
http://localhost:8089/
```

### Optimizations

- Optimize the Python code
- Re-write the query
- Tune the database
- Cache the result
- Buy more hardware

### Caching

- Redis install on docker

```bash
docker run -d -p 6379:6379 redis
```

### Severity
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL
