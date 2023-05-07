#!/bin/bash
# To messure cache misses
# perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations bash test.sh

./duckdb << EOF
.open file.db

SELECT * FROM employee_10000; 

EOF