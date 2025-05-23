import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
claude = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

def parse_prices_from_text(text_input):
    prompt = f"""
You are a price assistant. Extract a JSON list of products, prices, and suppliers from this text.

Input:
\"\"\"
{text_input}
\"\"\"

Output:
[
  {{
    "product_name": "Sugar",
    "price": 130,
    "supplier_name": "XYZ Traders"
  }},
  ...
]
"""

    response = claude.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=512,
        temperature=0.2,
        system="Extract product prices and supplier info for a shopkeeper app.",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text.strip()

