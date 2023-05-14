#!/bin/bash
# To messure cache misses
# perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations bash test.sh

./duckdb << EOF
.open file.db

SELECT COUNT(*) FROM employee_1;

EOF