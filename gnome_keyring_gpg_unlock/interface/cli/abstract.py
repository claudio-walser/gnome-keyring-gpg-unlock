import simpcli


class BaseCommand(object):
    interface = simpcli.Interface()
    cli = simpcli.Command()
    
    def run(self, secret: str, public_key: str):
        print('Needs to be implemented')