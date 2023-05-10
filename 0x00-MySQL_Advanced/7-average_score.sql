-- create stored procedure that computes and store avg score
DELIMITER ||
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN usr_id INT)
	BEGIN
		DECLARE avg_s FLOAT;
		SELECT AVG(score) FROM corrections WHERE user_id = usr_id INTO avg_s;
		UPDATE users SET average_score = avg_s WHERE users.id = usr_id;
	END; ||
DELIMITER ;
