-- Include your solutions to the More Practice problems in this file.



-- Insert a Brand
INSERT INTO brands 
    VALUES ('sub', 'Subaru', '1953', 'Tokyo, Japan');


-- Insert Models
INSERT INTO models (year, brand_id, name) 
    VALUES ('2015', 'che', 'Malibu');

INSERT INTO models (year, brand_id, name)
    VALUES ('2015', 'sub', 'Outback');


-- Create an Awards Table
CREATE TABLE awards(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    year INTEGER NOT NULL,
    winner_id INTEGER
        REFERENCES models);

-- Insert Awards

INSERT INTO awards (name, year, winner_id)
    VALUES ('IIHS Safety Award', '2015', '47');

INSERT INTO awards (name, year, winner_id)
    VALUES ('IIHS Safety Award', '2015', '48');

INSERT INTO awards (name, year)
    VALUES ('Best in Class', '2015');