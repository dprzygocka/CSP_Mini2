#!/bin/bash

# Run only once

./duckdb << EOF
.open file.db
.read duckdbdata/duckdb_main.sql
.read duckdbdata/employe_1.sql
.read duckdbdata/employe_10.sql
.read duckdbdata/employe_100.sql
.read duckdbdata/employe_1000.sql
.read duckdbdata/employe_10000.sql
.read duckdbdata/employe_100000.sql
.read duckdbdata/employe_1000000.sql
EOF