import python_terraform as terraform
import traceback

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from certs.apps import CertsConfig
from enum import Enum


class TFStatus(Enum):
    OK = 0
    ERR = 1
    DIFF = 2


class TFError(Exception):
    pass

class InitTFError(TFError):
    pass

class PlanTFError(TFError):
    pass

class Command(BaseCommand):
    help = 'Setup and initialize Vault PKI.'

    tf_path = str(settings.VAULT['TF_PATH'])
    tf_options = {
        'capture_output': False,
        'no_color': None,
    }
    tf_vars = {
        'address': settings.VAULT['URL'],
        'token': settings.VAULT['TOKEN'],
        'domains': ['redkiwi.root'],
        'roles': {
            'client': 'redkiwi_client',
            'server': 'redkiwi_server',
        },
    }

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest='cmd', required=True)
        parser_import = subparsers.add_parser('import')
        parser_import.set_defaults(func=self.tf_import)
        parser_apply = subparsers.add_parser('apply')
        parser_apply.set_defaults(func=self.tf_apply)

    def handle(self, *args, **options):
        self.tf = terraform.Terraform(working_dir=self.tf_path)
        try:
            ret, stdout, stderr = self.tf.init(**self.tf_options)
            if ret == TFStatus.ERR:
                raise InitTFError(f'result: {ret}')
            options['func'](*args, **options)
        except TFError as e:
            traceback.print_exc()
            print('Error occurred: {}'.format(e))


    def tf_import(self, *args, **options):
        tf_options = {
            **self.tf_options,
            'var': self.tf_vars,
        }

        tf_args_list = [
            ('vault_pki_secret_backend.pki', 'pki_openvpn'),
            ('vault_pki_secret_backend_role.client', 'pki_openvpn/roles/redkiwi_client'),
            ('vault_pki_secret_backend_role.server', 'pki_openvpn/roles/redkiwi_server'),
        ]
        for tf_args in tf_args_list:
            self.tf.import_cmd(*tf_args, **tf_options)

    def tf_apply(self, *args, **options):
        tf_options = {
            **self.tf_options,
            'skip_plan': True,
            'var': self.tf_vars,
        }
        ret, stdout, stderr = self.tf.apply(**tf_options)
        if ret == TFStatus.ERR:
            raise PlanTFError(f'result: {ret}')
