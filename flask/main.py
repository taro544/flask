from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_output():
    # Run external Python script and capture output
    output = subprocess.check_output(['python3', 'timer.py'])
    
    # Return output as JSON
    return jsonify({'output': output.decode('utf-8')})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
