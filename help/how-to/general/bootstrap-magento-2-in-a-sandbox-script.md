---
title: Bootstrap Adobe Commerce 2 in a sandbox script
description: 'To initialize an Adobe Commerce 2 application in a sample sandbox script, execute the following script from the Adobe Commerce root directory:'
exl-id: a6acb30a-5175-42c6-8de3-e80c9ae8dac1
---
# Bootstrap Adobe Commerce 2 in a sandbox script

To initialize an Adobe Commerce 2 application in a sample sandbox script, execute the following script from the Adobe Commerce root directory:

```php
<?php

error_reporting(E_ALL | E_STRICT);
ini_set('display_errors', 1);

require __DIR__ . '/app/bootstrap.php';
$bootstrap = \Magento\Framework\App\Bootstrap::create(BP, $_SERVER);
$objectManager = $bootstrap->getObjectManager();

//$model = $objectManager->get('Vendor\Module\Some\Model');
```
