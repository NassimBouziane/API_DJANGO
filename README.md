# API_DJANGO

## INSTALL
pip install django  
pip install djangorestframework
## RUN THE APP
```bash 
python manage.py runserver
```
### OR
django-admin runserver

## DATABASE SETUP
You can setup your database with settings and run
```bash 
python manage.py makemigrations 
```
```bash 
python manage.py migrate 
```
or just use the creation script

# REST API
### Products

```python
# Retrieve a list of all products
GET /api/products/

# Create a new product
POST /api/products/create/
Request Body: JSON object representing the product details
EXEMPLE : 
{
  "name": "Test",
  "category": 4,
  "brand": "Test",
  "size": 45,
  "price":10,
  "quantity": 1,
  "status": "Accepté"
}


# Retrieve details of a specific product
GET /api/products/<int:pk>/

# Update details of a specific product
PUT /api/products/<int:pk>/update/
Request Body: JSON object representing the updated product details


# Delete a specific product
DELETE /api/products/<int:pk>/delete/
```

### Categories
```python
# Retrieve a list of all categories
GET /categories/

# Create a new category
POST /categories/create/
Request Body: JSON object representing the category details
EXEMPLE : {
    "name":"Test"
    }

# Retrieve details of a specific category
GET /categories/<int:pk>/

# Update details of a specific category
PUT /categories/<int:pk>/update/
Request Body: JSON object representing the updated category details

# Delete a specific category
DELETE /categories/<int:pk>/delete/


```


### FILTERED PRODUCTS
```python 
GET /products/filter/?PARAMS=
params can be :
- name
- brand
- category
- size
- quantity
- status

```