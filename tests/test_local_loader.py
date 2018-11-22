from pathlib import Path

import pytest

from bye_bye_shopify.loaders import LocalLoader
from bye_bye_shopify.models import Product


@pytest.fixture
def loader():
    return LocalLoader()


def test_gets_product_path_prefix(loader):
    assert loader.get_product_path_prefix(Product(id=123)) == str(Path.cwd() / "data/products/123/123")
