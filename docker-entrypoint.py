import os

from subprocess import call

migrate = True if os.getenv("DB_MIGRATE", "true").lower() == "true" else False

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_wait = os.getenv("DB_WAIT", "3m")

if not db_host:
    raise ValueError("DB_HOST environment is not defined")

if not db_port.isnumeric():
    raise ValueError("DB_HOST environment is not defined")

if migrate:
    os.system(f"dockerize -wait tcp://{db_host}:{db_port} -timeout {db_wait}")
    os.system("flask db upgrade")

if os.getenv("PRINT_ENV", "false").lower() == "true":
    os.system("printenv")

os.system("dockerize -wait tcp://$DB_HOST:3306 -timeout 1m")
os.system("flask db upgrade")

if __name__ == "__main__":
    if os.getenv("DEBUG_INTEGRATION") == "vscode":
        call(["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "main", "--wait-for-client", "--multiprocess",
              "-m", "flask", "main", "-h", "0.0.0.0", "-p", os.getenv("API_PORT")])
    else:
        call(["python", "main.py", os.getenv("API_PORT")])
