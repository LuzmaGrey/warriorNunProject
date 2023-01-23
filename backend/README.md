# Backend

## What is this?
This is the backend portion of the website.  This is necessary as Javascript cannot make direct calls to other websites (i.e. change.org).  Those requests for the website must be routed through a separate server that can make the calls.  Then the responses will be redirected back tho the webpage.


## Dev Setup
1. Make sure you have Python 3.6.  Check the version by running ```python --version``` in the terminal.
2. Be in the backend folder
3. [Create a virtual environment](https://docs.python.org/3/library/venv.html) by running ``` python3 -m venv .```
4. Activate the virtual environment (venv)

    a. On mac this is done via ```source venv/bin/activate```
      
5. *THIS IS ALSO REQUIRED FOR THE ACTUAL WEBSITE TO MAKE THE AUTOMATIC UPDATES* Install the required packages into the virtual environment.  ``` pip install -r requirements.txt ```
6. Run ``` python routes.py ```
7. Test that it's working by going to ```localhost:5000```
8. When you're done, you can deactivate your virtual env by running ``` deactivate ```


## Endpoints

### For development, hostname is localhost:5000

hostname/petition_count
- Returns the weekly and total number of signatures on the petition 

hostname/gofundme
- Returns the current fund amount and the current goal
