from flask import Flask, render_template, request, jsonify
import os

from src.application.service import encrypt_text, decrypt_emojis, DEFAULT_MAPPING, SPACE_EMOJI

# Configura o diretório de templates de forma relativa a este arquivo
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html', mapping=DEFAULT_MAPPING, space=SPACE_EMOJI)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text'}), 400
    
    text = data['text']
    result = encrypt_text(text)
    return jsonify({'result': result})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    if not data or 'emojis' not in data:
        return jsonify({'error': 'Missing emojis'}), 400
    
    emojis = data['emojis']
    result = decrypt_emojis(emojis)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
