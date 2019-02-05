# ezplanner-flask-api

## Getting started
Run  the following command to clone this repository to your local machine.
```
git clone https://github.com/EZPlanner/ezplanner-flask-api
```

## Instructions
Please insure that python3.x is installed.  
Please ensure that qpdf is installed (ubuntu pacakge). This pacakge is used for transcript decrypting.  
Once the repo has been cloned, within a teminal inside that repo, create a virtualenv (EX. venv).  
pip install the dependencies.   
```
pip install -r requirements.txt
```
Export the flask variables.  
``` 
export FLASK_APP=run.py
export FLASK_ENV=developemnt
```
Run the development server.  
```
flask run
```
