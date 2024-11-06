---
title: During installation, exception SessionHandler::read()
description: "This article provides a fix for an exception **SessionHandler::read()** error during Adobe Commerce installation."
---

# During installation, exception SessionHandler::read()

This article provides a fix for an exception **SessionHandler::read()** error during Adobe Commerce installation.

## Issue

At the last step of installing Adobe Commerce, the following exception displays:

```temrinal
exception 'Exception' with message 'Warning: SessionHandler::read():
open(..) failed: No such file or directory (2) ../magento2/lib/internal/Magento/Framework/Session/SaveHandler.php on line 74'
in ../magento2/lib/internal/Magento/Framework/App/ErrorHandler.php:67
```

>[!NOTE]
>
>This error occurs only in code versions earlier than September 28, 2015. If you install code dated September 29 or later, this error should not occur. For more information about configuration options for Redis, see [Configure Redis](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cache/redis/config-redis) in our developer documentation. For more information about specifying Redis using the command-line installer, see the [installation topic](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/advanced) or the [deployment configuration topic](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/deployment) in our developer documentation.

## Cause

This happens when your `session.save_handler` PHP parameter is set to some another session storage than `files` (for example, `redis`, `memcached`, and so on). This is a known issue we're working to resolve.

## Solutions:

* Upgrade your Adobe Commerce code. Refer to [Installation Guide > Update the Adobe Commerce software](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/uninstall) in our developer documentation.
* Use the following workaround with existing code:

## Locate `php.ini` {#locate-php-ini}

Locate `php.ini` by entering the following command:

```php
php -i | grep "Loaded Configuration File"
```

Typical locations follow:

* Ubuntu: `/etc/php5/cli/php.ini`
* CentOS: `/etc/php.ini`

## Workaround {#workaround}

1. As a user with `root` privileges, open `php.ini` in a text editor.
1. Locate `session.save_handler`
1. Set it in any of the following ways:
    * To comment it out:

      ```php
      ;session.save_path = <path>
      ```
    
    * To set it to a file system path:
    
      ```php
      session.save_handler = files
      ```
