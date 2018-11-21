import json
import shutil
from abc import ABC, abstractmethod
from pathlib import Path
from urllib.parse import urlparse

import requests

from .config import config, log
from .models import Product


class Loader(ABC):

    @abstractmethod
    def load_product(self, product: Product):
        raise NotImplementedError()


class LocalLoader(Loader):
    base_dir: Path

    def __init__(self):
        self.base_dir = Path(config.local_loader_base_dir) if config.local_loader_base_dir else Path("./data").resolve()

    @property
    def products_dir(self) -> Path:
        return self.base_dir / "products"

    def product_dir(self, product: Product):
        return self.products_dir / config.product_dir_name_template.format(product=product)

    def load_product(self, product: Product):
        log.info(f"Loading {product.id}")
        product_dir = self.product_dir(product)
        if not product_dir.exists():
            product_dir.mkdir(parents=True)

        product_file = config.product_file_name_template.format(product=product)
        descr_file = (product_dir / (product_file + ".json"))
        with descr_file.open("w") as f:
            json.dump(product.to_dict(), f, sort_keys=True, indent=4)

        for image in product.images:
            image_file_suffix = Path(urlparse(image.src).path).suffix
            image_file = (product_dir / (product_file + f"-{str(image.position).zfill(2)}{image_file_suffix}"))
            if image_file.exists():
                log.debug(f"{image.src} already downloaded to {image_file}, doing nothing")
                continue
            log.info(f"Downloading {image.src} to {image_file}")
            r = requests.get(image.src, stream=True)
            with open(image_file, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
