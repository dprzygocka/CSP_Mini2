#!/bin/bash
# To messure cache misses
# perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations bash test.sh

./duckdb << EOF
.open file.db

INSERT INTO employee_1 (first_name, last_name, gender, personal_email, ssn, birth_date, start_date, job_id, org_id, accrued_holidays, salary, bonus) VALUES ('Dagmara', 'Garczynska', 'F', 'kamila@example.com', '769-04-1996', '1990-01-16', '2022-01-08', '3', '4', '13', '1400000', '47000');


EOF