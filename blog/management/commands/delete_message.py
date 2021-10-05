from django.core.management.base import BaseCommand
from blog.models import ContactModel

class Command(BaseCommand):
    help = 'Verilən email adresinə görə gələn mesajları sil'
    
    def add_arguments(self, parser):
        parser.add_argument('--email', help='Email adresi daxil edin.')
        
    def handle(self, **options):
        if options.get('email') is None:
            ContactModel.objects.all().delete()
            self.stdout.write('Mesajlar silindi.')
        
        else:
            ContactModel.objects.filter(email=options.get('email')).delete()
            self.stdout.write('Mesajları silindi: '+options.get('email'))
