CREATE TABLE employee (
    id int not null,
    first_name varchar(100),
    last_name varchar(100),
    gender varchar(1),
    personal_email varchar(100),
    ssn varchar(20),
    birth_date date,
    job_id int not null,
    office_id int not null,
    accrued_holidays smallint,
    salary int,
    bonus int,

    PRIMARY KEY(id),
    CONSTRAINT fk_employe
      FOREIGN KEY(job_id)
	  REFERENCES jobs(id));

CREATE TABLE jobs (
    id int not null,
    title varchar(100),
    min_salary int,
    max_salary int);

CREATE TABLE job_history (
    emp_id int not null,
    start_date date,
    job_id int not null,
    office_id int not null);

CREATE TABLE office (
    id int not null primary key,
    city varchar(100),
    org_id int not null);

CREATE TABLE org (
    id int not null primary key,
    title varchar(100));

