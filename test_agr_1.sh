#!/bin/bash
# To messure cache misses
# perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations bash test.sh

./duckdb << EOF
.open file.db

EXPLAIN ANALYZE UPDATE employee_1000000 SET last_name='Smith', WHERE first_name='Dagmara';

EOF