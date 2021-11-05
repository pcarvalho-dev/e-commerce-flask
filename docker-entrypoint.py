import os

from subprocess import call

# PRINT ENVIRONMENT VARIABLES
for k, v in os.environ.items():
    print(f'{k}={v}')

# os.system("dockerize -wait tcp://$DB_HOST:3306 -timeout 1m")
# os.system("flask db upgrade")

# RUN APP
if __name__ == "__main__":
    call(["python", "main.py"])
