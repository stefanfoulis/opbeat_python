from opbeat.utils.compat import TestCase
from opbeat.contrib.pylons import Opbeat


def example_app(environ, start_response):
    raise ValueError('hello world')


class MiddlewareTest(TestCase):
    def setUp(self):
        self.app = example_app

    def test_init(self):
        config = {
            'opbeat.servers': 'http://localhost/api/store',
            'opbeat.organization_id': 'p' * 32,
            'opbeat.app_id': 'p' * 32,
            'opbeat.secret_token': 'a' * 32,
        }
        middleware = Opbeat(self.app, config)
