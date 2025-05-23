from flask import Flask, render_template, request, jsonify
from supabase_client import supabase
from claude_client import parse_prices_from_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_manual():
    product = request.form['product']
    price = float(request.form['price'])
    supplier = request.form['supplier']

    supplier_id = supabase.table("suppliers").select("*").eq("name", supplier).execute().data
    if not supplier_id:
        supplier_id = supabase.table("suppliers").insert({"name": supplier}).execute().data[0]['id']
    else:
        supplier_id = supplier_id[0]['id']

    product_id = supabase.table("products").insert({"name": product}).execute().data[0]['id']
    supabase.table("prices").insert({
        "product_id": product_id,
        "supplier_id": supplier_id,
        "price": price,
        "source_type": "manual"
    }).execute()

    return jsonify({"success": True})

@app.route('/ai-parse', methods=['POST'])
def ai_parse():
    raw_text = request.form.get('raw_text')
    if not raw_text:
        return jsonify({"error": "No text input"}), 400

    structured = parse_prices_from_text(raw_text)
    return jsonify({"structured_data": structured})

if __name__ == '__main__':
    app.run(debug=True)
