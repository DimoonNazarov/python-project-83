DROP TABLE IF EXISTS urls;
DROP TABLE IF EXISTS urls_checks;

CREATE TABLE urls (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE urls_checks (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        URL_ID INT REFERENCES urls(id),
        status_code int,
        h1 varchar(255),
        title varchar(255),
        description varchar(255),
        created_at timestamp NOT NULL
);
