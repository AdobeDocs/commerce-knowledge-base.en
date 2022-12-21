---
title: "Modules missing from Adobe Commerce 2.4.4"
description: This article provides a solution for the issue when modules included in previous Adobe Commerce versions are not present in 2.4.4.
---

# Modules missing from Adobe Commerce 2.4.4

This article provides a solution for when modules included in previous Adobe Commerce versions are not present in 2.4.4.

## Affected products and versions

* Adobe Commerce (all deployment methods) all  [supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## Issue

You cannot install a module or have found that some core extensions are not present when you upgraded to Adobe Commerce 2.4.4. This should only result from installing a module that requires one of the bundled extensions removed from Adobe Commerce 2.4.4.

Scenario 1: The project has utilized one of the core bundled module's functionality. The utilized bundled module is not included in Adobe Commerce 2.4.4. 
Scenario 2: You have a module installed in your current version of Adobe Commerce that has 3rd party modules that extend or require that mdoule. This module is not present in Adobe Commerce 2.4.4. 

Scenario 1: After successfully upgrading to Adobe Commerce 2.4.4 you realize that the module and its provided functionality are missing.

Scenario 2: You have a module installed in your current project that has a dependency of one of the removed bundled modules.

This is expected behavior as the Vendor-Bundled Extensions have been removed from the Adobe Commerce 2.4.4 code base. 

## Solution

Install/purchase the official extensions separately. These are available on the [Commerce Marketplace](https://marketplace.magento.com/extensions.html).

## Related reading

* [Vendor-Bundled Extensions](https://experienceleague.adobe.com/docs/commerce-operations/release/notes/adobe-commerce/2-4-4.html?lang=en#vendor-bundled-extensions) in _Release Information_ in Adobe Commerce Documentation.
