-- Examples of queries.
USE books; -- to set the database you want to use.  Replace with any database name
SELECT * FROM books; -- or any table in the books database
INSERT INTO books (title, author, created_at, updated_at) VALUES ('Algorithm Challenges', 'Martin Puryear', NOW(), NOW());
DELETE FROM books WHERE id = 35;
UPDATE books SET author = 'Dan Brown' WHERE id = 34;
