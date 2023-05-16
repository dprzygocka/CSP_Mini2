#!/bin/bash

# Define database credentials
PGUSER=dagp
PGPASSWORD=mypass
PGDATABASE=mydb
PGHOST=localhost
TABLE=employee

for try in 1 2 3 4 5;
do

    for i in 1 10 100 1000 10000 100000;
    do
        # Run the query using psql
        # Define SQL query, update last index for employee
        SQL_QUERY="EXPLAIN ANALYZE select org.name,first_name, last_name, job_id from ${TABLE}_${i} e inner join org on e.org_id=org.id group by org.name,first_name, last_name, job_id;"

        psql "user=$PGUSER password=$PGPASSWORD dbname=$PGDATABASE host=$PGHOST" -c "$SQL_QUERY" | grep "Execution Time" | awk '{print $3}' >> ${try}_join.txt

    done


done