---
title: 'ACSD-48293: composite products out of stock when sold out child products restocked'
description: Apply the ACSD-48293 patch to fix the Adobe Commerce issue where the composite products go out of stock when the sold-out child products are returned to stock.
---
# ACSD-48293: composite products out of stock when sold out child products restocked

The ACSD-48293 patch fixes the issue where the composite products go out of stock when the sold-out child products are returned to stock. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.25 is installed. The patch ID is ACSD-48293. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.3-p3

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.3 - 2.4.4

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Composite products go out of stock when the child products that were sold out are returned to stock.

<u>Steps to reproduce</u>:

1. Create a secondary website, store, and store view.
1. Create two sources and stocks and assign them to each website.
1. Enable the show out-of-stock products option under **Store** > **Config** > **Catalog** > **Inventory** > **Stock Options** > **Display Out-of-Stock Products** = **Yes**.
1. Create a configurable product with one assoicated 
