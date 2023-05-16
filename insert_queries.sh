#!/bin/bash

# Define database credentials
PGUSER=dagp
PGPASSWORD=mypass
PGDATABASE=mydb
PGHOST=localhost
TABLE=employee

for try in 1 2 3 4 5;
do

    for n in 1 10 100 1000 10000 100000;
    do
        SQL_QUERY="DROP TABLE IF EXISTS employee_$n;"
            psql "user=$PGUSER password=$PGPASSWORD dbname=$PGDATABASE host=$PGHOST" -c "$SQL_QUERY"

        psql "user=$PGUSER password=$PGPASSWORD dbname=$PGDATABASE host=$PGHOST" -f ./postgres/employe_$n.sql
    done

    for i in 1 10 100 1000 10000 100000;
    do
        # Run the query using psql
        # Define SQL query, update last index for employee
        SQL_QUERY="EXPLAIN ANALYZE INSERT INTO ${TABLE}_${i} (first_name, last_name, gender, personal_email, ssn, birth_date, start_date, job_id, org_id, accrued_holidays, salary, bonus) VALUES ('Dagmara', 'Garczynska', 'F', 'kamila@example.com', '769-04-1996', '1990-01-16', '2022-01-08', '3', '4', '13', '1400000', '47000');"
        psql "user=$PGUSER password=$PGPASSWORD dbname=$PGDATABASE host=$PGHOST" -c "$SQL_QUERY" | grep "Execution Time" | awk '{print $3}' >> ${try}_insert.txt

    done
done