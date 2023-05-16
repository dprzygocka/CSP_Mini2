#!/bin/bash

# Define database credentials
PGUSER=dagp
PGPASSWORD=mypass
PGDATABASE=mydb
PGHOST=localhost
TABLE=employee
TRIES=$1
for try in $1;
do
    for i in 1 10 100 1000 10000 100000 1000000;
    do
    # Run the query using psql
        # Define SQL query
        SQL_QUERY="EXPLAIN ANALYZE SELECT * FROM ${TABLE}_${i};"
        psql "user=$PGUSER password=$PGPASSWORD dbname=$PGDATABASE host=$PGHOST" -c "$SQL_QUERY" | grep "Execution Time" | awk '{print $3}' >> ${try}_output_${i}.txt
    done
done