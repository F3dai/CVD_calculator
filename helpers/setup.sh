sudo apt-get update && sudo apt-get upgrade
sudo apt install python3-pip mysql-server
PWD=$(pwd)
pip3 install -r $PWD/requirements.txt
sudo bash -c 'sudo mysql < "$PWD/init.sql"'
#FLASK_APP=app.py FLASK_ENV=development flask run
#template_folder='template' flask run
flask run
