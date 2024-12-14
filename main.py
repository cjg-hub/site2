from flask import Flask, send_from_directory

app = Flask(__name__)
app.secret_key = 'fsdfm09283jdij12jd0s12'

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=True)
