CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make VARCHAR(45) NOT NULL,
    model VARCHAR(45) NOT NULL,
    color VARCHAR(45),
    v_type INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (v_type) REFERENCES vehicle_type(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE vehicle_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64)
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
)   VALUES (
    "Brett",
    "Bryant",
    "Darts"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
)   VALUES (
    "Jane",
    "Doe",
    "Skiing"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
)   VALUES (
    "John",
    "Doe",
    "Playing chess"
);

INSERT INTO vehicle_type (description) VALUES ("Motorcyle"); 
INSERT INTO vehicle_type (description) VALUES ("Car");
INSERT INTO vehicle_type (description) VALUES ("Truck");
INSERT INTO vehicle_type (description) VALUES ("SUV");

INSERT INTO vehicle (
    make,
    model,
    color,
    v_type,
    user_id
) VALUES (
    "Ford",
    "F250",
    "Gun Metal",
    3,
    1
);

INSERT INTO vehicle (
    make,
    model,
    color,
    v_type,
    user_id
) VALUES (
    "Chevy",
    "Silverado",
    "Blue",
    4,
    2
);

INSERT INTO vehicle (
    make,
    model,
    color,
    v_type,
    user_id
) VALUES (
    "Yamaha",
    "Sport",
    "Black",
    1,
    3
);

INSERT INTO vehicle (
    make,
    model,
    color,
    v_type,
    user_id
) VALUES (
    "Toyota",
    "Camry",
    "Red",
    2,
    4
);

INSERT INTO vehicle (
    make,
    model,
    color,
    v_type,
    user_id
) VALUES (
    "Toyota",
    "Tacoma",
    "Forest Green",
    3,
    1
);

SELECT  user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.color,
        vehicle.v_type AS vehicle_type
FROM user INNER JOIN vehicle 
ON user.id = vehicle.user_id;

SELECT  user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.color,
        vehicle_type.description
FROM user 
INNER JOIN vehicle ON user.id = vehicle.user_id
INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;