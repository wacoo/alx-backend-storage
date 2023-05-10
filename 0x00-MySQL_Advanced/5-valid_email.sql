-- create trigger that resets valid_email only when email changed
DROP TRIGGER IF EXISTS email_tr;
DELIMITER |

CREATE TRIGGER email_tr BEFORE UPDATE ON users
    FOR EACH ROW
    BEGIN
        IF OLD.email != NEW.email THEN
            SET NEW.valid_email = 0;
        END IF;
    END; |
DELIMITER ;
