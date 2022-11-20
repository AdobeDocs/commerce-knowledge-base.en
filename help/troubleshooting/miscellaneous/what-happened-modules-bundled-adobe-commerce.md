---
title: "Modules missing from Adobe Commerce 2.4.4"
description: This article provides a solution for the issue when modules included in previous Adobe Commerce versions are not present in 2.4.4.
---

# Modules missing from Adobe Commerce 2.4.4

This article provides a solution for when modules included in previous Adobe Commerce versions are not present in 2.4.4.

## Affected products and versions

* Adobe Commerce (all deployment methods) all  [supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## Issue

You cannot install a module or have found that some core extensions are not present when you upgraded to Adobe Commerce 2.4.4.

<u>Steps to reproduce</u>:

You try to install a module, as part of installing Adobe Commerce 2.4.4.

<u>Expected result</u>:

You successfully install the module.

<u>Actual result</u>:

You have the following error message when you run `composer update` in the terminal: _Your requirements could not be resolved to an installable set of packages_. 

Or when running the command: `bin/magento setup:upgrade` in the terminal you see an error that indicates the module was not install. For example:

_Service with name "Magento\Setup\Console\Command\DbStatusCommand" could not be created. Reason: Class "Vertex\Tax\Setup\Schema\Triggers\MigrateVertexInvoiceSent" does not exist_ 

## Cause

The Vendor-Bundled Extensions have been removed from the Adobe Commerce 2.4.4 code base. 

## Solution

Install/purchase the official extensions separately. These are available on the [Commerce Marketplace](https://marketplace.magento.com/extensions.html).

## Related reading

* [Vendor-Bundled Extensions](https://experienceleague.adobe.com/docs/commerce-operations/release/notes/adobe-commerce/2-4-4.html?lang=en#vendor-bundled-extensions) in _Release Information_ in Adobe Commerce Documentation.
