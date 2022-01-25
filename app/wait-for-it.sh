#!/bin/sh
# wait-for-postgres.sh

#export PATH=/run/postgresql:$PATH
set -e


shift

until PGPASSWORD=1234 psql -h database -U postgres -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec "$@"