#!/bin/bash

# Define database credentials
PGUSER=dagp
PGPASSWORD=mypass
PGDATABASE=mydb
PGHOST=localhost
TABLE=employee

for try in 1 2 3 4 5;
do

    for i in 1 10 100 1000 10000 100000 1000000;
    do
        # Run the query using psql
        # Define SQL query, update last index for employee
        SQL_QUERY="select * from ${TABLE}_${i} where job_id=1;"

        psql "user=$PGUSER password=$PGPASSWORD dbname=$PGDATABASE host=$PGHOST" -c "$SQL_QUERY" | grep "Execution Time" | awk '{print $3}' >> ${try}_select_all_where.txt
        { perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations psql "user=$PGUSER password=$PGPASSWORD dbname=$PGDATABASE host=$PGHOST" -c "$SQL_QUERY"; } 2>&1 | grep "cache-misses" | awk '{print $1}' >> ${try}_select_all_where_perf_cache.txt

    done


done