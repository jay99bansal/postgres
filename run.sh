export POSTGRES_INSTALLDIR="/home/jay/Desktop/CS 631/Course_project/postgres/install/"
export POSTGRES_SCRDIR="/home/jay/Desktop/CS 631/Course_project/postgres/"
cd "${POSTGRES_SCRDIR}"
export LD_LIBRARY_PATH="${POSTGRES_INSTALLDIR}"lib:${LD_LIBRARY_PATH}
export PATH="${POSTGRES_INSTALLDIR}"bin:${PATH}
export PGDATA="${POSTGRES_INSTALLDIR}"data
pg_ctl -D "$PGDATA" -l logfile start


create index ind1 on bookings.airports_data using gist(coordinates);

[['(1,1)', '2017-06-21', '9999-12-31'], ['(1,2)', '2017-05-03', '2018-10-08'], ['(1,1)', '2014-03-07', '2014-07-07'], ['(3,4)', '2017-05-03', '2018-10-08'], ['(2,7)', '2018-10-08', '9999-12-31'], ['(1,3)', '2014-07-07', '2017-05-03'], ['(7,8)', '2014-07-07', '9999-12-31'], ['(5,6)', '2017-06-21', '2019-01-01'], ['(3,4)', '2019-01-01', '9999-12-31'], ['(1,4)', '2014-03-07', '2019-01-01'], ['(7,10)', '2019-01-01', '9999-12-31'], ['(5,6)', '2014-07-07', '2018-10-08']]

