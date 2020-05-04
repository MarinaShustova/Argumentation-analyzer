import uuid
import re


class Argument:

    def __init__(self, template_text):
        self.id = uuid.uuid4()
        self.parameters = []
        self.text = template_text
        self.extract_parameters()

    def extract_parameters(self):
        open_par = [m.start() for m in re.finditer('\[', self.text)]
        close_par = [m.start() for m in re.finditer('\]', self.text)]
        for i in range(len(open_par)):
            extracted_string = self.text[open_par[i]+1:-1*(len(self.text)-close_par[i])]
            if not self.parameters.__contains__(extracted_string):
                self.parameters.append(extracted_string)
        print(self.parameters)


if __name__ == '__main__':
    arg = Argument('Вакцина от [вирус] - это проще сказать, чем сделать [вирус]')
