import uuid
from dao import Dao


class TemplatesDao(Dao.Dao):

    def get_templates(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM templates')
        records = cursor.fetchall()
        cursor.close()
        return records

    def add_template(self, name):
        cursor = self.get_cursor()
        id = uuid.uuid4()
        cursor.execute('INSERT INTO templates VALUES ({0}, {1})'.format(id, name))
        cursor.close()

    def get_template_by_id(self, id):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM templates WHERE id={}'.format(id))
        res = cursor.fetchone()
        cursor.close()
        return res
