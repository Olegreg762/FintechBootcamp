--loading data for card holder 2 and 18 from the database

SELECT * FROM transact 
NATURAL JOIN credit_card 
WHERE credit_card.cardholder_id IN ('2','18')

--Query to comapre anomalous transaction amounts to merchchant id for correlation for cardholder 18

SELECT * FROM transact 
NATURAL JOIN credit_card 
WHERE credit_card.cardholder_id IN ('18') AND
transact.amount >'300'

--Query to see if high number of transactions under $2.00 for card holder 18

SELECT * FROM transact 
NATURAL JOIN credit_card 
WHERE credit_card.cardholder_id IN ('18') AND
transact.amount <'2'

--Query to see if high number of transactions under $2.00 for card holder 2

SELECT * FROM transact 
NATURAL JOIN credit_card 
WHERE credit_card.cardholder_id IN ('2') AND
transact.amount <'2'

--loading data of daily transactions from jan to jun 2018 for card holder 25

SELECT * FROM transact 
NATURAL JOIN credit_card 
WHERE credit_card.cardholder_id IN ('25') AND
transact.date_ BETWEEN '2018-01-02 02:06:21' AND
'2018-06-30 03:05:55'

--query for identifying merchants

SELECT * FROM merchant
INNER JOIN merchant_cat 
ON merchant.merch_id IN ('64','87')

--

SELECT tran_id, date_, amount, cardholder_id 
FROM transact 
NATURAL JOIN credit_card 