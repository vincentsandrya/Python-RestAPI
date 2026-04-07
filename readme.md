<!-- virtual envi -->
python -m venv venv
venv\Scripts\activate

pip install fastapi uvicorn
pip install sqlalchemy psycopg2-binary python-dotenv

uvicorn main:app --reload

STEP : 
1. buat models
2. buat service
3. buat schema (response model)

http://127.0.0.1:8000/docs#/