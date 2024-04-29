---
title: "'Deployment failed with correct access keys in env:COMPOSER_AUTH or auth.json'"
description: This article provides a solution for the issue when deployment fails with the following error "The https://repo.magento.com/archives/magento/module-customer-balance/magento-module-customer-balance-100.4.0.0.zip file could not be downloaded (HTTP/1.1 404 Not Found)".
feature: Deploy
role: Developer
---
# Deployment failed: There are no commands defined in the 'cache' namespace error

>[!WARNING]
>
>Backup the database first, if you are doing this in a live Production site, before performing these steps.

This article provides a solution for the issue when your deployment fails with the following error:

```
W:   [Composer\Downloader\TransportException]
W:   The "https://repo.magento.com/archives/magento/module-customer-balance/magento-module-customer-balance-100.4.0.0.zip" file could not be downloaded (HTTP/1.1 404 Not Found)
```

## Affected products and versions

Adobe Commerce on cloud infrastructure 2.4.x

## Issue  

<u>Steps to reproduce</u>:

Attempt to deploy. 

<u>Expected results</u>:

You deploy successfully.

<u>Actual results</u>:

You do not deploy successfully. You see the following error *The "https://repo.magento.com/archives/magento/module-customer-balance/magento-module-customer-balance-100.4.0.0.zip" file could not be downloaded (HTTP/1.1 404 Not Found)*.

### Cause

The specified composer access keys found in one of these locations may not have access to the code:

* in the [!UICONTROL env:COMPOSER_AUTH] variable on the Project-level
* in the [!UICONTROL auth.json file], which takes precedence over the [!UICONTROL env:COMPOSER_AUTH variable].

### Solution

Update the [!UICONTROL env:COMPOSER_AUTH] variable on the Project-level and ensure that it is configured with keys that do have access to the code.

For steps, refer to [Variable levels](/docs/commerce-cloud-service/user-guide/configure/env/variable-levels) in Commerce on Cloud Infrastructure Guide. 

## Related reading

* [Adobe Commerce on cloud repo could not be accessed: 403 Forbidden or 404 Not Found error when deploying](/docs/commerce-knowledge-base/kb/troubleshooting/deployment/magento-commerce-cloud-repo-could-not-be-accessed-403-forbidden-or-404-not-found-error-when-deploying.html)
* [Deployment error: error 7 while downloading … port 443: Connection refused](/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/deployment-error-downloading-connection-refused-adobe-commerce.html)
