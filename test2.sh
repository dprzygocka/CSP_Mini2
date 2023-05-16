#!/bin/bash
# To messure cache misses
# perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations bash test.sh >> 1_duckdb_cache_select_all.txt

./duckdb << EOF
.open file.db
#1 SELECT ALL
#SELECT * from employee_1;
#SELECT * from employee_10;
#SELECT * from employee_100;
#SELECT * from employee_1000;
#SELECT * from employee_10000;
#SELECT * from employee_100000;
#SELECT * from employee_1000000;

#2 SELECT ALL WHERE
#SELECT * from employee_1 where job_id=1;
#SELECT * from employee_10 where job_id=1;
#SELECT * from employee_100 where job_id=1;
#SELECT * from employee_1000 where job_id=1;
#SELECT * from employee_10000 where job_id=1;
#SELECT * from employee_100000 where job_id=1;
#SELECT * from employee_1000000 where job_id=1;

#3 SELECT 1,2 WHERE
#SELECT first_name, last_name from employee_1 where job_id=1;
#SELECT first_name, last_name from employee_10 where job_id=1;
#SELECT first_name, last_name from employee_100 where job_id=1;
#SELECT first_name, last_name from employee_1000 where job_id=1;
#SELECT first_name, last_name from employee_10000 where job_id=1;
#SELECT first_name, last_name from employee_100000 where job_id=1;
#SELECT first_name, last_name from employee_1000000 where job_id=1;

EOF
