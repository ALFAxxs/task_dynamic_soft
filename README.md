
Create virutal environment
```
python -m venv venv
```

Activate virutal environment for Windows
```
venv\Scripts\Activate
```
Activate virutal environment for Linux/MacOS
```
source venv\bin\activate
```

Install dependencies
```python
pip install -r requirements.txt
```

Make migrations
```python

python manage.py makemigraionts
```

Migrate all migrations
```python
python manage.py migrate
```

Run development server
```python
python manage.py runserver
```