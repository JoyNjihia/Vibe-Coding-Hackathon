
CREATE TABLE suppliers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL
);

CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL
);

CREATE TABLE prices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID REFERENCES products(id),
    supplier_id UUID REFERENCES suppliers(id),
    price DECIMAL NOT NULL,
    date_reported TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source_type TEXT,
    raw_input TEXT
);
