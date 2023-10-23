# SQL Helper

This program helps to create a decision tree from sql queries used during a guessing game to guess a chosen movie in a database of movies.

## How to run

1. Replace the sql queries in the ``` sql_files ``` folder.
2. Clone the ``` .env.example ``` file and rename to ``` .env ``` and replace your database credentials
3. Create a virtual environment and install the requirements with the following command:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
4. Run the program:
```
python SQL_helper.py
```