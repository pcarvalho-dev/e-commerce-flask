import os

from application import create_app

app = create_app()
port = os.environ.get('API_PORT', '5000')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
