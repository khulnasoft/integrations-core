#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" khulnasoft_test <<-EOSQL
    CREATE TABLE persons (personid SERIAL, lastname VARCHAR(255), firstname VARCHAR(255), address VARCHAR(255), city VARCHAR(255));
    INSERT INTO persons (lastname, firstname, address, city) VALUES ('Cavaille', 'Leo', 'Midtown', 'New York'), ('Someveryveryveryveryveryveryveryveryveryverylongname', 'something', 'Avenue des Champs Elysees', 'Beautiful city of lights');
    SELECT * FROM persons;
    SELECT * FROM persons;
    SELECT * FROM persons;
EOSQL
