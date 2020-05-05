from dao import TemplatesDao

class TemplatesService:
    def addTemplate(self):
        print(1)

    def get_templates(self):
        t_dao = TemplatesDao.TemplatesDao()
        templates = t_dao.get_templates()
        return templates


