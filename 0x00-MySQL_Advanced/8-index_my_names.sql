-- create index of the first letter of name on tablle names
DROP INDEX idx_name_first ON names;
CREATE INDEX idx_name_first ON names(name(1));
