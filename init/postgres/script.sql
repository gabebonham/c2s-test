CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE automobile (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100),
    color VARCHAR(50),
    door_number INTEGER,
    price NUMERIC(12, 2),
    driver_name VARCHAR(80),
    size NUMERIC(5,2),
    weight NUMERIC(7,2),
    wheel_number INTEGER,
    year INTEGER,
    brand VARCHAR(80),
    created_at TIMESTAMP
);
