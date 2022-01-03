import os

file_dump = "initdb/dumps/ecommerce_db.sql"
os.system("docker-compose exec -T mysql mysqldump --set-gtid-purged=OFF --skip-add-locks -uroot -proot ecommerce_db > " + file_dump)
os.system(f"gzip -f " + file_dump)
