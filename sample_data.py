from datetime import datetime
import logging
from app import db
from app.models import Contact

try:
    db.session.query(Contact).delete()
    db.session.commit()
except Exception:
    db.session.rollback()

try:
    db.session.add(Contact(
        pid=2,
        name='Fred K',
        address='123 Main St',
        expiration=datetime.strptime('2023-01-01', "%Y-%m-%d").date(),
        entered = datetime.strptime('2023-01-01', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=450,
        name='Joe B',
        address='9970 NW. Hall Street',
        expiration=datetime.strptime('2024-12-13', "%Y-%m-%d").date(),
        entered = datetime.strptime('2018-01-03', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=3457834,
        name='Barack O',
        address='55 County Lane',
        expiration=datetime.strptime('2019-06-01', "%Y-%m-%d").date(),
        entered = datetime.strptime('2017-01-01', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=25,
        name='Wendy B',
        address='12 Talbot St',
        expiration=datetime.strptime('2023-04-11', "%Y-%m-%d").date(),
        entered = datetime.strptime('2020-01-01', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=893274,
        name='Don T',
        address='52 Garden Ave',
        expiration=datetime.strptime('2021-09-29', "%Y-%m-%d").date(),
        entered = datetime.strptime('2018-02-01', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=2,
        name='Abby R',
        address='551 Gregory Lane',
        expiration=datetime.strptime('2022-03-10', "%Y-%m-%d").date(),
        entered = datetime.strptime('2019-01-01', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=854269,
        name='George B',
        address='8359 Baker Rd',
        expiration=datetime.strptime('2023-11-09', "%Y-%m-%d").date(),
        entered = datetime.strptime('2019-01-01', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=5646,
        name='Bill C',
        address='9351 Shore Lane',
        expiration=datetime.strptime('2025-01-01', "%Y-%m-%d").date(),
        entered = datetime.strptime('2017-12-01', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=123467,
        name='Ron R',
        address='7 Wentworth Dr',
        expiration=datetime.strptime('2023-02-20', "%Y-%m-%d").date(),
        entered = datetime.strptime('2018-02-11', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=78653,
        name='George B',
        address='8783 Cherry St',
        expiration=datetime.strptime('2022-02-19', "%Y-%m-%d").date(),
        entered = datetime.strptime('2020-11-01', "%Y-%m-%d").date()))

    db.session.add(Contact(
        pid=523454,
        name='Jim C',
        address='120 N Edgemont St',
        expiration=datetime.strptime('2022-11-15', "%Y-%m-%d").date(),
        entered = datetime.strptime('2018-03-10', "%Y-%m-%d").date()))

except Exception as e:
    logging.error("Error adding rows: %s", e)

try:
    db.session.commit()
except Exception as e:
    logging.error("Session commit: %s", e)
    db.session.rollback()  