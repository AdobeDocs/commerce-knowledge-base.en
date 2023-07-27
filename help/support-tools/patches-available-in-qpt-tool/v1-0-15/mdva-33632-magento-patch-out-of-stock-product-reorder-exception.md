---
title: 'MDVA-33632 patch: out of stock product reorder exception'
description: The MDVA-33632 patch solves the issue where an exception is thrown when trying to reorder an out of stock product.
exl-id: 4a970db4-a64c-49b5-8c5f-8b9c5cdd946f
feature: "Orders, Products"
role: Admin
---
# MDVA-33632 patch: out of stock product reorder exception

The MDVA-33632 patch solves the issue where an exception is thrown when trying to reorder an out of stock product.

This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.15 is installed. Please note that the issue is scheduled to be fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

 **The patch is created for Adobe Commerce version:** Adobe Commerce on cloud infrastructure 2.3.6

 **Compatible with Adobe Commerce versions:** Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.0 - 2.3.6-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Steps to reproduce</u>:

1. Create a configurable product with one option (Example: **color** = *red*) and set **qty** = *1*.
1. Create a customer, and place an order with this product, which at that moment will become **qty** = *0*.
1. Go to Admin, and try to reorder the previous order.

<u>Expected results</u>:

The customer gets the "*This product is out of stock.*" message for an out of stock product, as expected.

<u>Actual results</u>:

The customer gets the "*This product is out of stock.*" message, and `var/log/exception.log` contains a similar exception:

```php
[2020-12-09 00:17:36] report.CRITICAL: This product is out of stock. {"exception":"[object] (Magento\\Framework\\Exception\\LocalizedException(code: 0): This product is out of stock. at /vendor/magento/module-quote/Model/Quote.php:1711)"} []
```

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT tool, refer to the [Patches available in QPT](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section.
