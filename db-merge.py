import os


file_dump = "initdb/dumps/ecommerce_db.sql.gz"
os.system("sed -i -E 's/DB_MIGRATE=.*/DB_MIGRATE=false/g' .env")

os.system("docker-compose stop")
os.system("docker-compose up -d")
os.system("docker-compose exec api flask db merge heads")
os.system("docker-compose exec -T mysql mysqldump --set-gtid-purged=OFF --skip-add-locks -uroot -proot ecommerce_db > " + file_dump)
os.system(f"gzip -f initdb/dumps/ecommerce_db.sql")
