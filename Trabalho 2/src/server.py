from flask import Flask
import ssl

app = Flask(__name__)


@app.route('/')
def home():
    return "Servidor HTTPS ativo e seguro!"


if __name__ == '__main__':
    context = ('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', port=4433, ssl_context=context)


