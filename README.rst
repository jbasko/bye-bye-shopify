===============
bye-bye-shopify
===============

If your Shopify store isn't doing too well, it's time to close it, but Shopify doesn't
provide an easy way to extract all your product catalogue. This Python utility allows
you to do that. I wrote it for and tested it only on my mom's candle store.

Configuration
-------------

In Shopify Admin, set up a private app and get an API key and password for it.

.. code-block:: shell

    export BYE_BYE_API_KEY="..."
    export BYE_BYE_API_PASSWORD="..."
    export BYE_BYE_API_HOSTNAME="..."

.. code-block:: shell

    python -m bye_bye_shopify.cli download_products
