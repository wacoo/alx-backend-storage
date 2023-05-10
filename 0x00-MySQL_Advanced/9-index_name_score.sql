--create index on the table names the first letter of name and score
DROP INDEX idx_name_first_score ON names;
CREATE INDEX idx_name_first_score ON names(name(1), score);
