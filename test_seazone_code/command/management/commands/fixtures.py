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

    def execute_load(self):
        """Procura pelo arquivo fixtures.txt (que contém as fixtures a serem instaladas)
        e executa o python manage.py loaddata de odas fixtures declaradas no arquivo.
        """
        # Start operation
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
