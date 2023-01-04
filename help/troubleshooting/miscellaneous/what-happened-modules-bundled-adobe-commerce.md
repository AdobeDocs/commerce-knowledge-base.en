---
title: Modules missing from Adobe Commerce 2.4.4
description: This article provides a solution for the issue when modules included in previous Adobe Commerce versions are not present in 2.4.4.
exl-id: c0335b66-803b-44d7-b966-7d60a5f21d8d
---
# Modules missing from Adobe Commerce 2.4.4

This article provides a solution for when modules included in previous Adobe Commerce versions are not present in 2.4.4.

## Affected products and versions

* Adobe Commerce (all deployment methods) all  [supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## Issue

You cannot install a third-party module or have found that some of the core bundled extensions are not present when you upgraded to Adobe Commerce 2.4.4. This should only result from installing a third-party module that requires one of the bundled extensions removed from Adobe Commerce 2.4.4 or if the project utilizes some of the functionality of one of the removed modules.

* Scenario 1: The project has utilized one of the core bundled module's functionality. The utilized bundled module is not included in Adobe Commerce 2.4.4. After successfully upgrading to Adobe Commerce 2.4.4, you realize that the module and its provided functionality are missing.

* Scenario 2: You have a module installed in your current project that has a dependency on one of the removed bundled modules. 

This is expected behavior as the Vendor-Bundled Extensions have been removed from the Adobe Commerce 2.4.4 code base. 

## Solution

Install/purchase the official extensions separately. These are available on the [Commerce Marketplace](https://marketplace.magento.com/extensions.html).

## Related reading

[Vendor-Bundled Extensions](https://experienceleague.adobe.com/docs/commerce-operations/release/notes/adobe-commerce/2-4-4.html?#vendor-bundled-extensions) in Adobe Commerce Documentation > Release Information > Adobe Commerce 2.4.4 release notes.
