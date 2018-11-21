from aarghparse import cli

from .config import configure_logging
from .loaders import LocalLoader
from .models import Product


@cli
def bye_bye_cli(subcommand, loader):

    @subcommand
    def download_products():
        for product in Product.get_all():
            loader.load_product(product)


if __name__ == "__main__":
    configure_logging()
    bye_bye_cli(loader=LocalLoader()).run()
