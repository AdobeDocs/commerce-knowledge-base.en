---
title: PHP version error or 404 error when accessing Adobe Commerce in browser
description: This article provides solutions for the issues where you cannot access your Adobe Commerce instance in a web browser and get 404 error or "unsupported PHP version" error.
exl-id: 6cfdeaae-5e52-411c-9006-5af8a467873a
feature: Configuration
role: Developer
---
# PHP version error or 404 error when accessing Adobe Commerce in browser

This article provides solutions for the issues where you cannot access your Adobe Commerce instance in a web browser and get 404 error or "unsupported PHP version" error.

## Affected products and versions:

* Adobe Commerce 2.3.x

## Issue: not supported PHP version

The following message displays when you try to access Adobe Commerce storefront or Commerce Admin:

 `Magento supports PHP 7.1.3 or later. Please read Magento System Requirements.`

### Solution

Try the following:

* Upgrade PHP to version 7.3. For more information see [Adobe Commerce 2.3 technology stack requirements](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/system-requirements) in our developer documentation.
* Restart Apache, since it might not be using the same PHP version as is on the file system. To restart Apache, use the following commands:
    * Ubuntu: `service apache2 restart`
    * CentOS: `service httpd restart`

## Issue: error 404

A 404 (Not Found) error displays when you try to access Adobe Commerce storefront or Commerce Admin.

### Solution

Try the following:

* Make sure [Apache server rewrites](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/web-server/apache) are enabled. If Apache server rewrites are set incorrectly, static files aren't served from the correct location.
* There might be an issue with the base URL you entered during the installation. You specify the base URL as the value of `--base-url=` when installing Adobe Commerce from the command line or as the value of the **Your Store Address** field on the Web Configuration page of the web installer. The base URL *must* start with the scheme (such as `http://` ) and end with a trailing slash (/). Run the installer again with a valid value and try accessing Adobe Commerce afterward.
