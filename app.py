from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

# Encoding Functions
def encode_base64(data):
    return base64.b64encode(data.encode()).decode()

def encode_hex(data):
    return data.encode().hex()

def encode_ascii_decimal(data):
    return ' '.join(str(ord(char)) for char in data)

def encode_ascii_binary(data):
    return ' '.join(format(ord(char), '08b') for char in data)

def encode_ascii_hex(data):
    return ' '.join(format(ord(char), 'x') for char in data)

# Decoding Functions
def decode_base64(data):
    return base64.b64decode(data.encode()).decode()

def decode_hex(data):
    return bytes.fromhex(data).decode()

def decode_ascii_decimal(data):
    return ''.join(chr(int(num)) for num in data.split())

def decode_ascii_binary(data):
    return ''.join(chr(int(num, 2)) for num in data.split())

def decode_ascii_hex(data):
    return ''.join(chr(int(num, 16)) for num in data.split())

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    text = data.get("text")
    encoding_type = data.get("encodingType")
    action = data.get("action")

    if not text:
        return jsonify({"result": "No input provided"})

    try:
        if encoding_type == "base64":
            result = encode_base64(text) if action == "encode" else decode_base64(text)
        elif encoding_type == "hex":
            result = encode_hex(text) if action == "encode" else decode_hex(text)
        elif encoding_type == "ascii-decimal":
            result = encode_ascii_decimal(text) if action == "encode" else decode_ascii_decimal(text)
        elif encoding_type == "ascii-binary":
            result = encode_ascii_binary(text) if action == "encode" else decode_ascii_binary(text)
        elif encoding_type == "ascii-hex":
            result = encode_ascii_hex(text) if action == "encode" else decode_ascii_hex(text)
        elif encoding_type == "decimal-ascii":
            result = decode_ascii_decimal(text)
        elif encoding_type == "binary-ascii":
            result = decode_ascii_binary(text)
        elif encoding_type == "hex-ascii":
            result = decode_ascii_hex(text)
        else:
            result = "Invalid encoding type"
    except Exception as e:
        result = f"Error: {str(e)}"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
