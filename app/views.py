from datetime import datetime
from flask import render_template, redirect, url_for, request
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterEqual, FilterGreater, FilterSmaller
from flask_appbuilder import ModelView, MultipleView, expose, BaseView, has_access
from flask_babel import lazy_gettext as _
from . import appbuilder, db

from .models import Contact
from .widgets import StandardListWidget, ImportedList
from .record_importer import RecordImporter

from werkzeug.utils import secure_filename

TEMP_CSV_FILENAME = "temp.csv"
DATE_FORMAT_STRING = "%Y-%m-%d"

class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)
    base_order = ('expiration','asc')
    

    label_columns = {'contact_group':'Data Group', 'pid':'ID', 'flagged_expiration':'Date Expired', 'entered':'Date Entered'}
    add_exclude_columns = ['temporary','included']
    edit_exclude_columns = ['temporary','included']
    search_exclude_columns = ['temporary','included']
    list_columns = ['pid','name','flagged_expiration','entered','address']


class PermanentContacts(ContactModelView):
    list_widget = StandardListWidget
    base_filters = [['temporary', FilterEqual, False]]

    @expose('/clear_temp/')
    @has_access
    def clear_temp(self):
        RecordImporter.clear_temp_records()
        return redirect(url_for('PermanentContacts.list'))

class IncludedCertifiedContacts(ContactModelView):
    list_widget = ImportedList
    list_title = "Certified records found in database"
    base_filters = [['temporary', FilterEqual, True],
                    ['included', FilterEqual, True],
                    ['expiration', FilterGreater, datetime.now()]]

class IncludedUncertifiedContacts(ContactModelView):
    list_widget = ImportedList
    list_title = "Uncertified records found in database"
    base_filters = [['temporary', FilterEqual, True],
                    ['included', FilterEqual, True],
                    ['expiration', FilterSmaller, datetime.now()]]

class ExcludedUncertifiedContacts(ContactModelView):
    list_widget = ImportedList
    list_title = "Uncertified records not found in database"
    base_filters = [['temporary', FilterEqual, True],
                    ['included', FilterEqual, False],
                    ['expiration', FilterSmaller, datetime.now()]]

class MultipleViewsExp(MultipleView):
    list_template = "multiple_views.html"
    views = [IncludedCertifiedContacts, IncludedUncertifiedContacts, ExcludedUncertifiedContacts]


class UploadView(BaseView):
    default_view = "import_csv"

    @expose('/import_csv/', methods = ['GET', 'POST'])
    def upload_file(self):
        if request.method == 'POST':
            f = request.files['file']
            f.save(secure_filename(TEMP_CSV_FILENAME))
            RecordImporter.clear_temp_records()
            RecordImporter.import_compare_csv(filepath=TEMP_CSV_FILENAME,date_format=DATE_FORMAT_STRING)
            return redirect(url_for('MultipleViewsExp.list'))

    @expose('/import_csv/')
    @has_access
    def import_csv(self):
        return self.render_template('upload.html')


db.create_all()
appbuilder.add_view(
    PermanentContacts,
    "Contacts Database",
    icon = "fa-envelope")
appbuilder.add_view_no_menu(IncludedCertifiedContacts())
appbuilder.add_view_no_menu(IncludedUncertifiedContacts())
appbuilder.add_view_no_menu(ExcludedUncertifiedContacts())
appbuilder.add_view_no_menu(MultipleViewsExp())
appbuilder.add_view_no_menu(UploadView())


"""
    Application wide 404 error handler
"""

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
