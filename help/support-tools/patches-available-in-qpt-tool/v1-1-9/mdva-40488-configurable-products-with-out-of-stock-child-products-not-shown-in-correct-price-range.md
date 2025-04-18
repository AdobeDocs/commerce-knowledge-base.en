---
title: 'MDVA-40488: Configurable products with out-of-stock child products not shown in correct price range'
description: The MDVA-40488 patch solves the issue where configurable products with out-of-stock child products are not shown in their correct price range. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.9 is installed. The patch ID is MDVA-40488. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.4.
exl-id: 0c4b9f5e-ae41-409e-b244-1d7cf948ed6f
feature: Configuration, Orders, Products
role: Admin
---
# MDVA-40488: Configurable products with out-of-stock child products not shown in correct price range

The MDVA-40488 patch solves the issue where configurable products with out-of-stock child products are not shown in their correct price range. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.9 is installed. The patch ID is MDVA-40488. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.4.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.2-p1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.2 - 2.4.3-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Configurable products with out-of-stock child products are not shown in their correct price range.

<u>Prerequisites</u>:

Go to the Commerce Admin > **stores** > **configuration** > **catalog** > **Inventory** > **stock options** and set **Display Out of Stock Products** configuration to *Yes*.

<u>Steps to reproduce</u>:

1. Create a configurable product with two associated products. For example: simple products Red and Brown.
1. Set inventory of the simple product Red, and set Stock Status to *In Stock*, then set the Enable Product status to *No*.
1. Set inventory of the simple product Brown, then set the Enable Product status to *Yes*.
1. Make sure the configurable product Stock Status is *In Stock*.
1. Change the inventory of the simple product Brown to 0 and set the Stock Status to *Out of Stock*.
1. At this point, the configurable product Stock Status is still *In Stock*.
1. Perform reindex.
1. Check the `min_price` and `max_price` for the configurable product in the `catalog_product_index_price` DB table - the two values are set to 0.
1. But if we set the configurable product Stock Status to *Out of stock* and do reindex, then we can see non-zero `min_price` and `max_price` values of the configurable product.

<u>Expected results</u>:

If all child products are *Out of Stock* and the configurable product itself is also *Out of Stock*, the price is calculated by using all the child products.

<u>Actual results</u>:

The `min_price` and `max_price` values for the configurable product in the `catalog_product_index_price` DB table are set to 0 when the configurable stock status is *In stock*, but if it's *Out of Stock* they become non-zero values.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/usage) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in our developer documentation.
