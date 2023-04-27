# This is a sample Python script.
import datetime
from random import randint

from faker import Faker
from faker.generator import random

import sys
import os


if len(sys.argv) >= 3:
    file_first_name = sys.argv[1]
    table_name = sys.argv[2]
    os.makedirs(os.path.dirname(file_first_name), exist_ok=True)
else:
    file_first_name = "postgres/postgres_main.sql"
    table_name = "employee"
    os.makedirs(os.path.dirname(file_first_name), exist_ok=True)

title_and_salary_range = {'Engineer': [90, 120], 'Senior Engineer': [110, 140], 'Manager': [130, 150],
                          'Associate': [60, 80], 'VP': [150, 250]}

offices = ['New York', 'Austin', 'Seattle', 'Chicago']
# codify the hierarchical structure
allowed_orgs_per_office = {'New York': ['Sales'], 'Austin': ['Devops', 'Platform', 'Product', 'Internal Tools'],
                           'Chicago': ['Devops'], 'Seattle': ['Internal Tools', 'Product']}


def first_name_and_gender():
    g = 'M' if random.randint(0, 1) == 0 else 'F'
    n = fake.first_name_male() if g == 'M' else fake.first_name_female()
    return {'gender': g, 'first_name': n}


def birth_and_start_date():
    sd = fake.date_between(start_date="-20y", end_date="now")
    delta = datetime.timedelta(days=365 * randint(18, 40))
    bd = sd - delta

    return {'birth_date': bd, 'start_date': sd}


def title_office_org():
    allowed_titles_per_org = {
        'Devops': ['Engineer', 'Senior Engineer', 'Manager'],
        'Sales': ['Associate'],
        'Platform': ['Engineer'],
        'Product': ['Manager', 'VP'],
        'Internal Tools': ['Engineer', 'Senior Engineer', 'VP', 'Manager']
    }

    office = random.choice(offices)
    org = random.choice(allowed_orgs_per_office[office])

    org_index = 0
    found_index = -1
    for index, item in enumerate(offices):
        list_of_orgs = allowed_orgs_per_office[item]
        for i in list_of_orgs:
            if i == org and item == office:
                found_index = org_index + 1
                break
            org_index = org_index + 1
    title = random.choice(allowed_titles_per_org[org])
    return {'office': office, 'title': title, 'org': found_index}


def salary_and_bonus():
    salary = round(random.randint(90000, 120000) / 1000) * 1000
    bonus_ratio = random.uniform(0.15, 0.2)
    bonus = round(salary * bonus_ratio / 500) * 500
    return {'salary': salary, 'bonus': bonus}


def title_office_org_salary_bonus():
    position = title_office_org()
    position_index = 1 + list(title_and_salary_range.keys()).index(position['title'])
    salary_range = title_and_salary_range[position['title']]

    salary = round(random.randint(1000 * salary_range[0], 1000 * salary_range[1]) / 1000) * 1000
    bonus_ratio = random.uniform(0.15, 0.2)
    bonus = round(salary * bonus_ratio / 500) * 500
    position.update({'salary': salary, 'bonus': bonus})
    position.update({'title': position_index})
    return position


# Press the green button in the gutter to run the script.
def add_insert_script_to_main_table(file_name, name_of_table, data_to_insert):
    sql = "INSERT INTO " + name_of_table + " (first_name, last_name, gender, personal_email, ssn, birth_date, start_date, " \
                                           "job_id, org_id, accrued_holidays, salary, bonus) VALUES (" \
                                           "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');" \
        .format(data_to_insert[1], data_to_insert[2], data_to_insert[0], data_to_insert[3], data_to_insert[4],
                data_to_insert[5], data_to_insert[6], data_to_insert[8], data_to_insert[9], data_to_insert[12],
                data_to_insert[10], data_to_insert[11])

    writer_append_file(file_name, sql)


def insert_postgres_table_creation():
    #"CREATE DATABASE testdb;"

    #writer_write_new_file(file_first_name, sql)

    sql = "CREATE TABLE job ( id int not null primary key, title varchar(100), min_salary int, max_salary int);"

    writer_write_new_file(file_first_name, sql)

    sql = "ALTER TABLE job ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY ( SEQUENCE NAME public.job_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1);"

    # write SQL statement to file
    writer_append_file(file_first_name, sql)

    sql = "CREATE TABLE office ( id int not null primary key, city varchar(100));"

    writer_append_file(file_first_name, sql)

    sql = "ALTER TABLE office ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY ( SEQUENCE NAME public.office_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1);"

    writer_append_file(file_first_name, sql)

    sql = "CREATE TABLE org ( id int not null primary key, name varchar(100), office_id int not null, CONSTRAINT fk_org FOREIGN KEY(office_id) REFERENCES office(id) );"

    writer_append_file(file_first_name, sql)

    sql = "ALTER TABLE org ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY ( SEQUENCE NAME public.org_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1);"

    writer_append_file(file_first_name, sql)

    for key, value in title_and_salary_range.items():
        insert_default_jobs(key, 1000 * value[0], 1000 * value[1])

    for index, item in enumerate(offices):
        insert_default_offices(item)
        list_of_orgs = allowed_orgs_per_office[item]
        for i in list_of_orgs:
            insert_default_orgs(i, index + 1)


def insert_default_jobs(title, min_salary, max_salary):
    sql = "INSERT INTO public.job (title, min_salary, max_salary) VALUES ('{}', '{}', '{}');" \
        .format(title, min_salary, max_salary)

    writer_append_file(file_first_name, sql)


def insert_default_orgs(name, office_id):
    sql = "INSERT INTO public.org (name, office_id) VALUES ('{}', '{}');".format(name, office_id)

    writer_append_file(file_first_name, sql)


def insert_default_offices(city):
    sql = "INSERT INTO public.office (city) VALUES ('{}');" \
        .format(city)

    writer_append_file(file_first_name, sql)


def writer_write_new_file(file_name, sql_command):
    # write SQL statement to file
    with open(file_name, 'w') as f:
        f.write(sql_command)
        f.write("\n")


def writer_append_file(file_name, sql_command):
    # write SQL statement to file
    with open(file_name, 'a') as f:
        f.write(sql_command)
        f.write("\n")


def set_up_main_employee(file_name, name_of_table):
    sql = "CREATE TABLE " + name_of_table + " (id int not null primary key, first_name varchar(100), last_name varchar(100), gender " \
                                            "varchar(1), personal_email varchar(100), ssn varchar(20), birth_date date, " \
                                            "start_date date, org_id int not null, job_id int not null, " \
                                            "accrued_holidays smallint, salary int, bonus int, CONSTRAINT fk_" + name_of_table + " FOREIGN KEY(job_id) REFERENCES job(id) , CONSTRAINT fk_" + name_of_table + "_org FOREIGN KEY(org_id) REFERENCES org(id) ); "

    writer_write_new_file(file_name, sql)

    sql = "ALTER TABLE " + name_of_table + " ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY ( SEQUENCE NAME public." + name_of_table + "_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1);"

    writer_append_file(file_name, sql)


def create_x_employees(name, number):
    file_n = "postgres/employe_" + str(number) + ".sql"
    tbl_n = name + "_" + str(number)
    set_up_main_employee(file_n, tbl_n)
    for _ in range(number):
        deep_list = [list(d[k]().values()) for k in d.keys()]
        row = [item for sublist in deep_list for item in sublist]
        add_insert_script_to_main_table(file_n, tbl_n, row)


if __name__ == '__main__':

    fake = Faker()
    # generate fake data
    d = dict()
    d['first_name_and_gender'] = first_name_and_gender
    d['last_name'] = lambda: {'last_name': fake.last_name()}
    d['personal_email'] = lambda: {'email': fake.email()}
    d['ssn'] = lambda: {'ssn': fake.ssn()}
    d['birth_and_start_date'] = birth_and_start_date
    d['title_office_org_salary_bonus'] = title_office_org_salary_bonus
    d['accrued_holidays'] = lambda: {'accrued_holiday': random.randint(0, 20)}

    insert_postgres_table_creation()

    create_x_employees(table_name, 1)
    create_x_employees(table_name, 10)
    create_x_employees(table_name, 100)
    create_x_employees(table_name, 1000)
    create_x_employees(table_name, 10000)
    create_x_employees(table_name, 100000)
    create_x_employees(table_name, 1000000)
