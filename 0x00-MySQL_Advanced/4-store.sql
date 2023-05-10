-- create trigger decreases the quantity of an item after adding a new order
DROP TRIGGER IF EXISTS items_tr;
CREATE TRIGGER items_tr AFTER INSERT ON orders
    FOR EACH ROW
        UPDATE items
            SET quantity = (quantity - NEW.number)
            WHERE name = NEW.item_name;
