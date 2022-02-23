DEBIAN_FRONTEND=noninteractive sudo apt-get update -y && sudo apt-get upgrade -y
DEBIAN_FRONTEND=noninteractive sudo apt install python3-pip mysql-server python3-flask -y
pip3 install -r requirements.txt
sudo bash -c 'sudo mysql < "helpers/init.sql"'
FLASK_APP=app/views.py FLASK_ENV=development flask run


#find . -name __pycache__ -exec rm -rf {} \;
#python3 -m pytest -vv
