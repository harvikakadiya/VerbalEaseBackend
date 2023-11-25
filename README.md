# VerbalEase- All in one Writing Assistant

## First Run

initiliaze a file named .env and place OPENAI_API_KEY which will be used to used as a GPT-3 key.
e.x: OPENAI_API_KEY="xxxxxxxxxxxxx"

1. Create virtual environment
```
py -m venv venv
```

2. Activate virtual environment

linux: 
```
source venv/bin/activate
```
windows: 
```
venv/scripts/activate 
```

3. Install dependency files
```
pip install -r requirements.txt
```

4. Run 
```
py main.py | python main.py
```

## APIS

1. Pharaphrase Text
- accepts key value type string as a form-data

2. Summarize Text
- accepts key value type string as a form-data

3. Translate Text
- accepts key value type string as a form-data

4. AI Chat Text
- accepts key value type string as a form-data
