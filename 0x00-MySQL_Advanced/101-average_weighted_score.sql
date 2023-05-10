-- create stored procedure that computes and stores the
-- avg weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER ||
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
	BEGIN
		DECLARE total_w_score INT;
		DECLARE w_score INT;
		UPDATE users SET average_score = (
			SELECT SUM(corrections.score * projects.weight) /SUM(projects.weight)
			FROM corrections
			INNER JOIN projects
			ON projects.id = corrections.project_id
			WHERE corrections.user_id = users.id);
		-- SELECT SUM(projects.weight) FROM corrections INNER JOIN projects ON projects.id = corrections.project_id INTO w_score;
		-- UPDATE users SET average_score = total_w_score / w_score;
	END; ||
DELIMITER ;
