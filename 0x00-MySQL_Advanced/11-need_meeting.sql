-- create view need_meeting that lists all students that score unde 80
-- and no last_meeting or more than a month
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS SELECT name FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
