SELECT * FROM customers
NATURAL JOIN orders;
-- Natural joins are sometimes used when:

-- The tables already contain logically related data designed with common column names and formats. In this case a natural join is convenient.

-- You want a quick ad-hoc join without typing a lot of SQL or looking up which columns to use.

-- You temporarily want to look at all possible combinations of related data sets without formally defining foreign keys.

-- You are joining database views which contain commonly named columns.

-- You want to emulate a join recommended by the query optimizer.

-- So in SUMMARY, for one-off simplified analysis, convenience for views, or prototyping, natural joins can be useful. But for most production systems, inner join with explicit ON logic is recommended for clarity, control, and maintenance.