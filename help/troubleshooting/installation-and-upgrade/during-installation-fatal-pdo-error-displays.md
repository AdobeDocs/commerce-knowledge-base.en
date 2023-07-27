---
title: During installation, fatal PDO error displays
description: This article provides a fix for an exception fatal PDO error during installation.
exl-id: d69908f0-71c9-48de-9369-6ada22f2b393
feature: Install, Upgrade
role: Developer
---
# During installation, fatal PDO error displays

This article provides a fix for an exception fatal PDO error during installation.

## Issue

```php
PHP Fatal error:  Class 'PDO' not found in /var/www/html/magento2/setup/module/Magento/Setup/src/Module/Setup/ConnectionFactory.php on line 44
```

## Solution

Make sure you install all the [required PHP extensions](https://devdocs.magento.com/guides/v2.4/install-gde/prereq/php-settings.html).
