# CVD calculator

Cardiovascular disease risk calculator for university project.

```
git clone https://github.com/F3dai/CVD_calculator.git
cd CVD_calculator
pip3 install -r requirements.txt
sudo mysql
source init.sql
exit
export FLASK_APP=cvd_app
export FLASK_ENV=development
flask run
```

## To do: 

 - ~~Hash passwords~~
 - Make all sql type/lengths proper
 - Refactor stuff
 - Statistics page
 - Add handling for duplicates (NHS ID?)
 - Untested - what happens when info is submitted for same NHS ID