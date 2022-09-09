from django.core.management.base import BaseCommand

from teachers.models import Teacher


class Command(BaseCommand):
    # help = 'generate teachers'

    def add_arguments(self, parser):
        # Optional argument
        parser.add_argument('-cnt', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        if kwargs['cnt']:
            if len(kwargs['cnt']) == 1 and kwargs['cnt'][0] >= 0:
                cnt = kwargs['cnt'][0]

                Teacher.gen_teachers(cnt)
                self.stdout.write('Command generate_teachers is done: ')
                tc = Teacher.objects.order_by('-pk')[:cnt]
                for i in tc:
                    self.stdout.write(f'{i}')
            else:
                self.stdout.write('ValueError')
        else:
            Teacher.gen_teachers()
            self.stdout.write('Command generate_teachers is done: ')
            tc = Teacher.objects.order_by('-pk')[:10]
            for i in tc:
                self.stdout.write(f'{i}')
