.headers on
.mode column

-- 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
-- ex) SELECT column1, column2 .... FROM table_name AS alias_name WHERE [condition];
SELECT * FROM playlist_track AS "A" ORDER BY PlaylistId DESC LIMIT 5;

-- 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요.
SELECT * FROM tracks AS "B" ORDER BY TrackId ASC limit 5;

-- 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
SELECT A.PlaylistId, B.Name 
From playlist_track AS "A", tracks AS "B"
WHERE A.TrackId = B.TrackId 
ORDER BY PlaylistId DESC LIMIT 10;

-- 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
SELECT A.PlaylistId, B.Name
From playlist_track AS "A", tracks AS "B"
WHERE A.PlaylistId = 10 AND A.TrackId = B.TrackId
ORDER BY Name DESC LIMIT 5;

-- 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
SELECT COUNT(*) FROM tracks INNER JOIN artists ON artists.Name = tracks.Composer;

-- 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
SELECT COUNT(*) FROM tracks LEFT JOIN artists ON tracks.Composer = artists.Name;

-- 8. invoice_items 테이블의 데이터를 출력하세요.
SELECT InvoiceLineId, InvoiceID FROM invoice_items ORDER BY InvoiceId ASC LIMIT 5;

-- 9. invoices 테이블의 데이터를 출력하세요.
SELECT InvoiceId, CustomerId From invoices ORDER BY InvoiceId ASC LIMIT 5;

-- 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
SELECT A.InvoiceLineId, A.InvoiceId 
FROM invoice_items AS A INNER JOIN invoices AS B 
ON A.InvoiceId = B.InvoiceId 
ORDER BY A.InvoiceId DESC LIMIT 5;

-- 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
SELECT A.InvoiceID, A.CustomerId
FROM invoices AS A INNER JOIN customers AS B
ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC LIMIT 5;

-- 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
SELECT A.InvoiceLineId, A.InvoiceId, C.CustomerId 
FROM invoice_items AS A
JOIN invoices AS B ON A.InvoiceLineId = B.InvoiceId
JOIN customers AS C ON B.InvoiceId = C.CustomerId
ORDER BY A.InvoiceId DESC LIMIT 5;

-- 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
SELECT A.CustomerId, COUNT(*) AS "개수"
FROM customers AS A 
JOIN invoices AS B ON A.CustomerId = B.CustomerId
JOIN invoice_items AS C ON B.InvoiceId = C.InvoiceId
GROUP BY A.CustomerId
ORDER BY A.CustomerId ASC LIMIT 5;