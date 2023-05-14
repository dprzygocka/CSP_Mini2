#!/bin/bash
# To messure cache misses
# perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations bash test.sh
PGUSER=dagp
PGPASSWORD=mypass
PGDATABASE=mydb
PGHOST=localhost
TABLE=employee

SQL_QUERY="EXPLAIN (ANALYZE, TIMING OFF) UPDATE employee_1000000 SET last_name='Smith' WHERE first_name='Dagmara';"
psql "user=$PGUSER password=$PGPASSWORD dbname=$PGDATABASE host=$PGHOST" -c "$SQL_QUERY"
