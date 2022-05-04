from datetime import datetime
import logging
from app import db
from app.models import Contact
import csv

"""Helper class for handling CSV imports"""
class RecordImporter():
    
    def clear_temp_records():
        """Clears all temporary records from database"""
        try:
            db.session.query(Contact).filter(Contact.temporary==True).delete()
            db.session.commit()
        except Exception:
            db.session.rollback()

    def import_compare_csv(filepath, date_format):
        """Loads and parses CSV file. Rows are added to the database
        as Contact objects and flagged as temporary.

        filepath -- relative path to CSV file to import
        date_format -- format string for converting date string to Date object"""

        # Open file and create csvreader
        try:
            file = open(filepath)
            csvreader = csv.reader(file)
        except Exception as e:
            logging.error("CSV file failed to open: %s", e)

        # Parse header row and assign column numbers
        try:
            header = next(csvreader)
            header = [x.lower() for x in header]
            if ("pid" in header): pid_index = header.index("pid")
            if ("name" in header): name_index = header.index("name")
            if ("address" in header): address_index = header.index("address")
            if ("expiration" in header): expiration_index = header.index("expiration")
            if ("entered" in header): entered_index = header.index("entered")
        except Exception as e:
            logging.error("Bad CSV header: %s", e)

        # Parse remaining rows and add them to the database as Contact objects
        try:
            rows = []
            for row in csvreader:
                rows.append(row)
                c = Contact()
                c.pid = row[pid_index]
                c.name = row[name_index]
                c.address = row[address_index]
                c.expiration = datetime.strptime(row[expiration_index], date_format).date()
                c.entered = datetime.strptime(row[entered_index], date_format).date()
                c.temporary = True

                # Set flag to indicate if record is already in the database
                match = db.session.query(Contact).filter_by(pid=c.pid).first()
                if match is None:
                    c.included=False
                else:
                    c.included=True

                db.session.add(c)
                try:
                    db.session.commit()
                    print("inserted", c)
                except Exception as e:
                    logging.error("Creating Contact: %s", e)
                    db.session.rollback()      
            file.close()
        except Exception as e:
            logging.error("Error adding rows: %s", e)