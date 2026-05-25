# AI Circuit Fault Diagnosis

## Run
pip install -r requirements.txt

python pipelines/preprocess.py
python pipelines/train.py

uvicorn backend.main:app --reload
