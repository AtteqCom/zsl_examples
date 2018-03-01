from zsl import Zsl, inject
from zsl.application.containers.web_container import WebContainer
from zsl.application.modules.cli_module import ZslCli
from zsl.interface.web.performers.method import call_exposers_in_method_packages


def create_and_run_app():
    Zsl('HelloWorld', modules=WebContainer.modules())
    call_exposers_in_method_packages()

    @inject(zsl_cli=ZslCli)
    def run(zsl_cli: ZslCli) -> None:
        zsl_cli.cli()

    run()


if __name__ == "__main__":
    create_and_run_app()
