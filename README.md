# CVD calculator

Cardiovascular disease risk calculator for university project.

```
git clone https://github.com/F3dai/CVD_calculator.git
cd CVD_calculator
pip3 install flask mysql-connector-python
sudo mysql
source init.sql
exit
flask run
```

To auto-reload on development:

```
FLASK_APP=app.py FLASK_ENV=development flask run
```