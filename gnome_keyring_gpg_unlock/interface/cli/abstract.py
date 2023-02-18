import simpcli


class BaseCommand(object):
    interface = simpcli.Interface()

    def run(self, secret: str, public_key: str):
        print('Needs to be implemented')