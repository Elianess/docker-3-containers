CREATE TABLE IF NOT EXISTS mytable (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

COPY mytable (name) FROM '/var/lib/postgresql/data.txt';
