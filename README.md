[![Build Status](https://travis-ci.org/tanvir002700/tracker.svg?branch=master)](https://travis-ci.org/tanvir002700/tracker)
# tracker

## Database setup

$sudo su - postgres
$psql

CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';

ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

\q

exit

# run test
python manage.py test --pattern='*test.py'
