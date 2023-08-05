CREATE TABLE IF NOT EXISTS categories (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    value DECIMAL(10, 2) NOT NULL DEFAULT 0.0,
    stock INT NOT NULL DEFAULT 0,
    category_id INTEGER UNSIGNED NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);