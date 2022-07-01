SELECT
    *
FROM
    flight
WHERE
    depdate BETWEEN date('2021-01-01') AND date('2022-01-01');