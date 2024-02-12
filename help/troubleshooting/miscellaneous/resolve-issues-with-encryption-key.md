---
title: Resolve issues with encryption key
description: This article talks about how to fix the issues caused by the encryption key not being moved together with DB dump to the other environment.
exl-id: 34410da0-1bd5-421e-9cd7-d3ee75ad8ed7
feature: Cache, Variables
role: Developer
---
# Resolve issues with encryption key

This article talks about how to fix the issues caused by the encryption key not being moved together with DB dump to the other environment.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x

## Issue

After importing a [database dump](/help/how-to/general/create-database-dump-on-cloud.md) from Production to Staging/Integration environments, saved credit card numbers appear wrong and/or payments fail for payment integrations requiring usage of merchant credentials.

## Cause

The encryption key used to encrypt sensitive data, like credit card numbers and merchant credentials, is not stored in the database, and therefore does not get transferred to other environment after database dump import/export.

## Solution

You need to copy the encryption key from the source environment and add it to the destination environment.

To copy the encryption key:

1. SSH to your project that was the source for the database dump, as described in [SSH to environment](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/secure-connections.html) in our developer documentation.
1. Open `app/etc/env.php` in a text editor.
1. Copy the value of `key` for `crypt`.

```php
return array ('crypt' =>      array ('key' => '<your encryption key>', ),);
```

To set the key value for the destination project:

1. Open the [Cloud Console](https://console.adobecommerce.com) and locate your project.
1. Set the value of the [CRYPT\_KEY](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-deploy.html) (in our developer documentation) variable, as described in [Configure your project](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/overview.html) in our developer documentation. This will trigger the deployment process and `CRYPT_KEY` will be overridden in the `app/etc/env.php` file on every deployment.

Optionally, you can manually override the encryption key in the `app/etc/env.php` file:

1. SSH to the destination environment.
1. Open `app/etc/env.php` in a text editor.
1. Paste the copied data as the `key` value for `crypt`.
1. Save the edited `env.php`.
1. Clean cache on the destination environment by running `bin/magento cache:clean` or in the Commerce Admin under **System** > **Tools** > **Cache Management**.
