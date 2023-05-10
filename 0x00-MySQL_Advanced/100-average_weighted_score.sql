-- create a stored procedure that computes and stores average weighted score
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER ||
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN usr_id INT)
	BEGIN
		DECLARE total_score INT;
		DECLARE total_weight INT;
		SELECT SUM(corrections.score * projects.weight) FROM corrections INNER JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = usr_id INTO total_score;
		SELECT SUM(projects.weight) FROM corrections INNER JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = usr_id INTO total_weight;
		UPDATE users SET average_score = (total_score / total_weight)  WHERE users.id = usr_id;
	END; ||
DELIMITER ;
