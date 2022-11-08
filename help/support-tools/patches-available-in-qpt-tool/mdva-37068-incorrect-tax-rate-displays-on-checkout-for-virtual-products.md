---
title: "MDVA-37068: Incorrect tax displayed on Checkout for virtual products"
description: "The MDVA-37068 patch fixes the issue when the Checkout Page displays an incorrect tax rate for virtual products. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.26 is installed. The patch ID is MDVA-37068. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.4."
---

# MDVA-37068: Incorrect tax displayed on Checkout for virtual products

The MDVA-37068 patch fixes the issue when the Checkout Page displays an incorrect tax rate for virtual products. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.26 is installed. The patch ID is MDVA-37068. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.4.

## Affected products and versions

**The patch is created for Adobe Commerce version:**
Adobe Commerce on cloud infrastructure 2.3.5-p2

**Compatible with Adobe Commerce versions:**
Adobe Commerce (all deployment methods) 2.3.1-2.4.2-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Incorrect tax rate is displayed on Checkout Page when the Shopping Cart has only virtual products.

<u>Prerequisites</u>:

1. Create two separate tax rates and tax rules for two different countries - for example 10% and 1%.
1. Create a virtual product.
1. Run reindex and clean cache.

<u>Steps to reproduce</u>:

1. Create a customer.
1. Add different billing and shipping addresses.
1. Add a virtual product to the cart.
1. Check the Cart and Checkout Page.

<u>Expected results</u>:

The tax displayed on the Cart and Checkout Page are the same.

<u>Actual results</u>:

The tax displayed on the Cart and Checkout Page are NOT the same.

## Apply the patch

To apply individual patches use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT tool, refer to the [Patches available in QPT tool](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section.