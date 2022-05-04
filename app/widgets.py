from flask_appbuilder.widgets import ListWidget


class StandardListWidget(ListWidget):
     template = 'widgets/standard_list.html'

class ImportedList(ListWidget):
     template = 'widgets/imported_list.html'
