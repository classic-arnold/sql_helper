source venv/bin/activate
export $(xargs < .env)
pip install -r requirements.txt
python SQL_helper.py