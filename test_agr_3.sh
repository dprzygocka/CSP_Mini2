#!/bin/bash
# To messure cache misses
# perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations bash test.sh

./duckdb << EOF
.open file.db

Select org.name,first_name, last_name, job_id, max(salary) from employee_1000 e inner join org on e.org_id=org.id group by org.name,first_name, last_name, job_id;

EOF