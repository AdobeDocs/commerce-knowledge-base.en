---
title: Cannot install using nginx
description: This article provides a fix for a failed Adobe Commerce installation, when using the nginx web server.
exl-id: 0af90c7e-0733-41c8-b217-9595b133fa95
feature: Install, Upgrade
role: Developer
---
# Cannot install using nginx

This article provides a fix for a failed Adobe Commerce installation, when using the nginx web server.

## Issue

If you use the nginx web server and you attempt to install the Adobe Commerce software, the installation sometimes fails.

## Solution

You can confirm the issue by the following error in the `var/report` directory:

```php
NOTE: You cannot install Adobe Commerce using the Setup Wizard because the Adobe Commerce setup directory cannot be accessed.
You can install Adobe Commerce using either the command line or you must restore access to the following directory: /var/www/html/setup
If you are using the sample nginx configuration, please go to http://ce.mtf03.bcn.magento.com/setup/";i:1;s:641:"#0 /var/www/html/lib/internal/Magento/Framework/App/Http.php(213): Magento\Framework\App\Http->redirectToSetup(Object(Magento\Framework\App\Bootstrap), Object(Exception))
```

### Workaround

Install the Adobe Commerce software using the [command line](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/advanced).
