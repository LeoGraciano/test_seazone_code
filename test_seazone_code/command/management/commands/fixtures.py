import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command class

    Esta classe, filha de BaseCommand, estende a funcionalidade do django
    de utilização de comandos customizados.
    Nesta, foi criado o comando para carregamento de fixtures.
    """
    help = 'Initializing services...'

    def add_arguments(self, parser):
        parser.add_argument('--load', help='Data load', action='store_true')

    def db_delete(self):
        os.system('find . -path "*/*.sqlite3" -delete')

    def migrate_delete(self):
        os.system('find . -path "*/migrations/*.py" -not -name "init.py" -delete')

    def migrate_create(self):
        os.system(
            'python manage.py makemigrations immobile reserve announcement && python manage.py migrate')

    def execute_load(self):
        """Procura pelo arquivo fixtures.txt (que contém as fixtures a serem instaladas)
        e executa o python manage.py loaddata de odas fixtures declaradas no arquivo.
        """
        # Start operation
        print(
            '\n', '*********************** remove db sqlite3....  ************************')
        self.db_delete()

        print(
            '\n', '*********************** remove old migrate....  ************************')
        self.migrate_delete()

        print(
            '\n', '*********************** create migrate ....  ************************')
        self.migrate_create()

        print('\n', '*********************** loading data ....  ************************')

        FILE = 'fixtures.txt'

        f = open(FILE, 'r')
        name_fixtures = f.readlines()

        for n in name_fixtures:
            os.system(f'python manage.py loaddata {n}')

        f.close()
        print('\n', '******************** Load done! *************************', '\n')

    def handle(self, *args, **options):
        MSG = 'The data load can be danger, removing data in database'
        YES_NO = 'Yes(Y) or No(N)'

        def confirm():
            _confirmation = input(f'{MSG} {YES_NO} ?  ')
            resp = ['Y', 'Yes']
            return _confirmation in resp

        if not confirm():
            print('!!!!!!!!!!! Canceled Operation  !!!!!!!!!!!!')
            return False

        self.execute_load()
