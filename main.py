# This is a sample Python script.
import datetime
from random import randint

from faker import Faker
from faker.generator import random

import sys

if len(sys.argv) >= 3:
    file_name = sys.argv[1]
    table_name = sys.argv[2]
    row_count = int(sys.argv[3])
    db_type = int(sys.argv[4])
else:
    file_name = "postgres.sql"
    table_name = "employee"
    row_count = 100
    db_type = 1  # 1 = postgres, 2 = duckdb


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
    # generate a map of real office to fake office
    offices = ['New York', 'Austin', 'Seattle', 'Chicago']
    # codify the hierarchical structure
    allowed_orgs_per_office = {'New York': ['Sales'], 'Austin': ['Devops', 'Platform', 'Product', 'Internal Tools'],
                               'Chicago': ['Devops'], 'Seattle': ['Internal Tools', 'Product']}
    allowed_titles_per_org = {
        'Devops': ['Engineer', 'Senior Engineer', 'Manager'],
        'Sales': ['Associate'],
        'Platform': ['Engineer'],
        'Product': ['Manager', 'VP'],
        'Internal Tools': ['Engineer', 'Senior Engineer', 'VP', 'Manager']
    }

    office = random.choice(offices)
    org = random.choice(allowed_orgs_per_office[office])
    title = random.choice(allowed_titles_per_org[org])
    return {'ofice': office, 'title': title, 'org': org}


def salary_and_bonus():
    salary = round(random.randint(90000, 120000) / 1000) * 1000
    bonus_ratio = random.uniform(0.15, 0.2)
    bonus = round(salary * bonus_ratio / 500) * 500
    return {'salary': salary, 'bonus': bonus}


def title_office_org_salary_bonus():
    position = title_office_org()
    title_and_salary_range = {'Engineer': [90, 120], 'Senior Engineer': [110, 140], 'Manager': [130, 150],
                              'Associate': [60, 80], 'VP': [150, 250]}
    salary_range = title_and_salary_range[position['title']]

    salary = round(random.randint(1000 * salary_range[0], 1000 * salary_range[1]) / 1000) * 1000
    bonus_ratio = random.uniform(0.15, 0.2)
    bonus = round(salary * bonus_ratio / 500) * 500
    position.update({'salary': salary, 'bonus': bonus})
    return position


# Press the green button in the gutter to run the script.
def createSQL(row):
    sql = "INSERT INTO " + table_name + " (first_name, last_name, gender, personal_email, ssn, birth_date, start_date, " \
                                        "office, title, org, accrued_holidays, salary, bonus) VALUES (" \
                                        "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');" \
        .format(row[1], row[2], row[0], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[12], row[10],
                row[11])

    # write SQL statement to file
    with open(file_name, 'a') as f:
        f.write(sql)
        f.write("\n")


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

    sql = "CREATE TABLE " + table_name + " (id int not null, first_name varchar(100), last_name varchar(100), gender " \
                                         "varchar(1), personal_email varchar(100), ssn varchar(20), birth_date date, " \
                                         "start_date date, office varchar(100), title varchar(100), org varchar(100), " \
                                         "accrued_holidays smallint, salary int, bonus int); "

    if db_type == 1:
        sql = "CREATE TABLE " + table_name + " (id int not null, first_name varchar(100), last_name varchar(100), gender " \
                                             "varchar(1), personal_email varchar(100), ssn varchar(20), birth_date date, " \
                                             "start_date date, office varchar(100), title varchar(100), org varchar(100), " \
                                             "accrued_holidays smallint, salary int, bonus int); "
        sql2 = "ALTER TABLE " + table_name + " ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY ( SEQUENCE NAME public.employee_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1);"
    else:
        sql = "CREATE SEQUENCE seq_personid START 1;"

        sql2 = "CREATE TABLE " + table_name + " (id integer primary key default nextval('seq_personid'), first_name varchar(100), last_name varchar(100), gender " \
                                             "varchar(1), personal_email varchar(100), ssn varchar(20), birth_date date, " \
                                             "start_date date, office varchar(100), title varchar(100), org varchar(100), " \
                                             "accrued_holidays smallint, salary int, bonus int); "

    # write SQL statement to file
    with open(file_name, 'w') as f:
        f.write(sql)
        f.write("\n")
        f.write(sql2)
        f.write("\n")

    for _ in range(row_count):
        deep_list = [list(d[k]().values()) for k in d.keys()]
        row = [item for sublist in deep_list for item in sublist]
        createSQL(row)
