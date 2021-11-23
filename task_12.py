class Worker:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 18:
            self.__age = age
        else:
            print("Слишком молодой работник для нашего журнала")

    name = property(get_name, set_name)
    age = property(get_age, set_age)


class Article:
    def __init__(self, name, subject, author):
        self.__name = name
        self.__subject = subject
        self.__author = author
        


class Writer(Worker):
    def __init__(self, name, age, field_of_activity):
        
        self.__name = name
        self.__age = age
        self.__field_of_activity = field_of_activity
        self.articles = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 18:
            self.__age = age
        else:
            print("Слишком молодой писатель для нашего журнала")

    def get_field_of_activity(self):
        return self.__field_of_activity

    def set_field_of_activity(self, field_of_activity):
        self.__field_of_activity = field_of_activity

    def create_article(self, name_article, subject):
        article = Article(name_article, subject, self)
        self.articles.append(article)

    def send_last_article(self, editor):
        if self.articles:
            editor.get_article(self.articles[-1])
        else:
            print("Статей у автора пока нет!")


class Editor:
    def __init__(self, name, age, field_of_activity):
        self.__name = name
        self.__age = age
        self.__field_of_activity = field_of_activity
        self.articles = []

    def get_article(self, article):
        self.articles.append(article)

    def check_article(self, journal):
        if self.articles:
            journal.get_article(self.articles[-1])


class Journal:
    def __init__(self, editor):
        self.editor = editor
        self.articles = []

    def get_article(self, article):
        self.article.append(article)
    