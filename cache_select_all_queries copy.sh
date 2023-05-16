#!/bin/bash
# To messure cache misses
# perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations bash test2.sh >> 1_duckdb_cache_select_all.txt

./duckdb << EOF
.open file.db
#1
#UPDATE employee_1 SET last_name='Testing' WHERE ssn='454-15-0847';
#UPDATE employee_10 SET last_name='Testing' WHERE ssn='137-63-5663';
#UPDATE employee_100 SET last_name='Testing' WHERE ssn='767-99-1703';
#UPDATE employee_1000 SET last_name='Testing' WHERE ssn='463-85-8967';
#UPDATE employee_10000 SET last_name='Testing' WHERE ssn='125-96-6916';
#UPDATE employee_100000 SET last_name='Testing' WHERE ssn='758-92-6027';
#UPDATE employee_1000000 SET last_name='Testing' WHERE ssn='633-16-3675';

#1 delete
#DELETE FROM employee_1 WHERE ssn='454-15-0847';
#DELETE FROM employee_10 WHERE ssn='137-63-5663';
#DELETE FROM employee_100 WHERE ssn='767-99-1703';
#DELETE FROM employee_1000 WHERE ssn='463-85-8967';
#DELETE FROM employee_10000 WHERE ssn='125-96-6916';
#DELETE FROM employee_100000 WHERE ssn='758-92-6027';
#DELETE FROM employee_1000000 WHERE ssn='633-16-3675';

#middle
#UPDATE employee_1 SET last_name='Testing' WHERE ssn='454-15-0847';
#UPDATE employee_10 SET last_name='Testing' WHERE ssn='241-41-4413';
#UPDATE employee_100 SET last_name='Testing' WHERE ssn='578-88-0737';
#UPDATE employee_1000 SET last_name='Testing' WHERE ssn='860-69-2804';
#UPDATE employee_10000 SET last_name='Testing' WHERE ssn='825-01-5674';
#UPDATE employee_100000 SET last_name='Testing' WHERE ssn='291-47-5619';
#UPDATE employee_1000000 SET last_name='Testing' WHERE ssn='128-26-3343';

#middle delete
#DELETE FROM employee_1 WHERE ssn='454-15-0847';
#DELETE FROM employee_10 WHERE ssn='241-41-4413';
#DELETE FROM employee_100 WHERE ssn='578-88-0737';
#DELETE FROM employee_1000 WHERE ssn='860-69-2804';
#DELETE FROM employee_10000 WHERE ssn='825-01-5674';
#DELETE FROM employee_100000 WHERE ssn='291-47-5619';
#DELETE FROM employee_1000000 WHERE ssn='128-26-3343';


#last
#UPDATE employee_1 SET last_name='Testing' WHERE ssn='454-15-0847';
#UPDATE employee_10 SET last_name='Testing' WHERE ssn='759-21-1107';
#UPDATE employee_100 SET last_name='Testing' WHERE ssn='462-80-1347';
#UPDATE employee_1000 SET last_name='Testing' WHERE ssn='375-72-2853';
#UPDATE employee_10000 SET last_name='Testing' WHERE ssn='888-46-4823';
#UPDATE employee_100000 SET last_name='Testing' WHERE ssn='763-52-6574';
#UPDATE employee_1000000 SET last_name='Testing' WHERE ssn='253-17-6452';

#last delete
#DELETE FROM employee_1 WHERE ssn='454-15-0847';
#DELETE FROM employee_10 WHERE ssn='759-21-1107';
#DELETE FROM employee_100 WHERE ssn='462-80-1347';
#DELETE FROM employee_1000 WHERE ssn='375-72-2853';
#DELETE FROM employee_10000 WHERE ssn='888-46-4823';
#DELETE FROM employee_100000 WHERE ssn='763-52-6574';
#DELETE FROM employee_1000000 WHERE ssn='253-17-6452';

EOF
