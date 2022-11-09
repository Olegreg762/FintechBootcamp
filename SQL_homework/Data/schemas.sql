
CREATE TABLE merchant_cat (
merch_cat_id INT NOT NULL,
merch_name VARCHAR(50) 
);

CREATE TABLE transact (
tran_id INTEGER NOT NULL,
date_ timestamp without time zone DEFAULT now() NOT NULL,
amount FLOAT NOT NULL,
card_num VARCHAR(20) NOT NULL,
merch_id INT NOT NULL
);

CREATE TABLE credit_card (
card_num VARCHAR(20) NOT NULL,
cardholder_id INT NOT NULL
);

CREATE TABLE card_holder (
carholder_id INT NOT NULL,
cardholer_name CHARACTER VARYING(50) NOT NULL
);

CREATE TABLE merchant (
merch_id INT NOT NULL,
merch_name CHARACTER VARYING(50) NOT NULL,
merch_cat_id INT NOT NULL
);