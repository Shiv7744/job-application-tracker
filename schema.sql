CREATE TABLE applications (
    id SERIAL PRIMARY KEY,
    company VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    status VARCHAR(30) NOT NULL DEFAULT 'Applied',
    date_applied DATE NOT NULL,
    link TEXT,
    notes TEXT
);