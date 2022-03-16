from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["Make"] = result[1]
        res_dict["Model"] = result[2]
        res_dict["Color"] = result[3]
        res_dict["vehicle_type"] = result[4]
        res_dict["user_id"] = result[5]
        res_dict["active"] = result[6]
        out.append(res_dict)
    return out


def insert(Vehicle_dict):
    value_tuple = (
        Vehicle_dict["Make"],
        Vehicle_dict["Model"],
        Vehicle_dict["Color"],
    )

    stmt = """
        INSERT INTO vehicle (
            Make,
            Model,
            Color
        )   VALUES (?, ?, ?)
    """
    cursor = get_db()
    cursor.execute(stmt, value_tuple)
    cursor.commit()
    cursor.close()


def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_user_id(uid):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE user_id=?", (uid, ))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def deactivate_vehicle(pk):
    stmt = """
        UPDATE vehicle
        SET active=0
        WHERE user_id=?
    """
    cursor = get_db()
    cursor.execute(stmt, (pk,))
    cursor.commit()
    cursor.close()


def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data["Make"],
        vehicle_data["Model"],
        vehicle_data["Color"],
        pk
    )
    stmt = """
        UPDATE vehicle
        SET Make=?,
        Model=?,
        Color=?
        WHERE user_id=?
    """
    cursor = get_db()
    cursor.execute(stmt, value_tuple)
    cursor.commit()
