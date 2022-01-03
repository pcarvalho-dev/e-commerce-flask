echo "Init databases restore"
mysql -quiet -uroot -p$MYSQL_ROOT_PASSWORD -e 'create database ecommerce_db'

echo "Restoring ecommerce_db"
gunzip < /docker-entrypoint-initdb.d/dumps/ecommerce_db.sql.gz | mysql -quiet -uroot -p$MYSQL_ROOT_PASSWORD auto_conect_db
echo "Databases restore finished ;-)"
