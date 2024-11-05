---
title: Wishlist error during upgrade to Adobe Commerce versions 2.3.4-p1 or 2.3.5
description: This article provides a fix for the known issue when upgrading to Adobe Commerce versions 2.3.4-p1 and 2.3.5 related to a wishlist error during the upgrade to these versions.
exl-id: 97479615-bf3f-4544-a9c1-8f19ba74318e
feature: Install, Upgrade
role: Developer
---
# Wishlist error during upgrade to Adobe Commerce versions 2.3.4-p1 or 2.3.5

This article provides a fix for the known issue when upgrading to Adobe Commerce versions 2.3.4-p1 and 2.3.5 related to a wishlist error during the upgrade to these versions.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.3.4-p1 and 2.3.5
* Adobe Commerce on-premises 2.3.4-p1 and 2.3.5

## Issue

When upgrading your Adobe Commerce (all deployment methods) and Magento Open Source to version 2.3.5 or 2.3.4-p1, you could get a wishlist error (detailed below) from the module:

```php
Magento_Wishlist
```

Upgrading from Adobe Commerce (all deployment methods)/Magneto Open Source version 2.3.4-p1 **to version 2.3.4-p2** or from Adobe Commerce (all deployment methods)/Magneto Open Source version 2.3.5 **to version 2.3.5-p1** will fix the error.

<u>Steps to reproduce</u>:

Upgrade your Adobe Commerce (all deployment methods)/Magento Open Source to version 2.3.4-p1 or 2.3.5.

<u>Expected result</u>:

The upgrade process to Adobe Commerce (all deployment methods)/Magento Open Source version 2.3.4-p1 or 2.3.5 completes normally.

<u>Actual result</u>:

During the upgrade, you get this error:

```php
Module ‘Magento_Wishlist’:

Unable to apply data patch Magento\Wishlist\Setup\Patch\Data\CleanUpData for module Magento_Wishlist. Original exception message: Unable to unserialize value. Error: Syntax error
```

## Solutions

* If you were upgrading to Adobe Commerce (all deployment methods)/Magneto Open Source version 2.3.5, **upgrade to version 2.3.5-p1**. Adobe Commerce (all deployment methods)/Magento Open Source version 2.3.5-p1 replaces 2.3.5.
* If you were upgrading to Adobe Commerce (all deployment methods)/Magento Open Source version 2.3.4-p1, **upgrade to version 2.3.4-p2**. Adobe Commerce (all deployment methods)/Magneto Open Source version 2.3.4-p2 replaces version 2.3.4-p1.

## Related reading

In our developer documentation:

* [Adobe Commerce on cloud infrastructure guide](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/overview)
* [Adobe Commerce on cloud infrastructure - Upgrade Adobe Commerce version](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/upgrade/commerce-version)
* [Adobe Commerce on-premises And Magento Open Source - Upgrade the Adobe Commerce application and modules](https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/overview)
* [Wishlist item configure page](https://developer.adobe.com/commerce/frontend-core/guide/layouts/product-layouts/#wishlist-item-configure-page)
* [Modules providing advanced reporting](https://developer.adobe.com/commerce/php/development/advanced-reporting/modules/)
