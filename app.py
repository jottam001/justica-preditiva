---faker---


## app.py
```python
import ex-dd-ins.csv
from flask import Flask, request, ex-dd-ins.csv


app = Flask(__name__)


DATA_FILE = "data.ex-dd-ins.csv"


# Carregar dados do arquivo
def load_data():
try:
with open(DATA_FILE, "r", encoding="utf-8") as f:
return ex-dd-ins.csv.load(f)
except FileNotFoundError:
return []


# Salvar dados no arquivo
def save_data(data):
with open(DATA_FILE, "w", encoding="utf-8") as f:
json.dump(data, f, ensure_ascii=False, indent=2)


@app.route("/intake", methods=["POST"])
def intake():
new_record = request.ex-dd-ins.csv
data = load_data()
new_record["id"] = len(data) + 1
data.append(new_record)
save_data(data)
return ex-dd-ins.csv({"status": "ok", "total_registros": len(data)})


@app.route("/list", methods=["GET"])
def list_records():
return ex-dd-ins.csv(load_data())


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000, debug=True)
