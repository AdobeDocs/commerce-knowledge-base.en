---
title: 'MDVA-35197: GraphQL add to cart error if added products out of stock'
description: The MDVA-35197 patch fixes the issue where there's an error when adding to cart using GraphQL if previously added products become out of stock. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.17 is installed.
exl-id: 189312f7-a505-4ba4-b12d-662987e69374
feature: GraphQL
---
# MDVA-35197: GraphQL add to cart error if added products out of stock

The MDVA-35197 patch fixes the issue where there's an error when adding to cart using GraphQL if previously added products become out of stock. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.17 is installed.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.6

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.3.5 - 2.3.6-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Error when trying to add a product to cart via GraphQL if the other product already in the cart (also added via GraphQL) becomes out of stock.

<u>Steps to reproduce</u>:

1. Using GraphQL, add any product to the cart.
1. Log in to the Commerce Admin panel and set this product as out of stock.
1. Try adding another product to the cart via GraphQL.

<u>Expected results</u>:

In-stock products can be added to the cart.

<u>Actual results</u>:

GraphQL error message: *Some of the products are out of stock*. A new "in-stock" product cannot be added.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
