import sys
import os

# Add the parent directory to the path so we can import `app.sandbox_runner`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template, jsonify
from app.sandbox_runner import run_in_sandbox  # make sure this exists

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.form['code']
    print("[*] Received code:\n", code)

    try:
        output = run_in_sandbox(code)
        print("[*] Execution output:\n", output)
    except Exception as e:
        output = f"Error: {str(e)}"
        print("[!] Error during execution:", e)

    return jsonify({'output': output})


if __name__ == '__main__':
    app.run(debug=True)
