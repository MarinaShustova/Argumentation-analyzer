import uuid
from Dao import Dao


class ArticlesDao(Dao):

    def get_articles(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM articles')
        records = cursor.fetchall()
        cursor.close()
        return records

    def add_article(self, name, path):
        cursor = self.get_cursor()
        id = uuid.uuid4()
        cursor.execute('INSERT INTO articles VALUES ({0}, {1}, {2})'.format(id, name, path))
        cursor.close()

    def get_article_by_id(self, id):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM articles WHERE id={}'.format(id))
        res = cursor.fetchone()
        cursor.close()
        return res

if __name__ == '__main__':
    print(ArticlesDao().get_articles())
