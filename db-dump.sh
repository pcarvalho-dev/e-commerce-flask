#!/bin/bash

docker-compose exec -T mysql mysqldump -uroot -proot ecommerce_db > initdb/dumps/ecommerce_db.sql
cd initdb/dumps
gzip -f ecommerce_db.sql