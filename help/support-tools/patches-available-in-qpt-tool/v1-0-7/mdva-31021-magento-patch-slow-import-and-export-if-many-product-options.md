---
title: 'MDVA-31021: slow import and export if many product options'
description: The MDVA-31021 patch solves the issue when Import/Export takes longer than expected with large numbers of product options. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.7 is installed.
exl-id: d294b30d-b734-4bd6-bf1a-c116b789a63c
---
# MDVA-31021: slow import and export if many product options

The MDVA-31021 patch solves the issue when Import/Export takes longer than expected with large numbers of product options. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.7 is installed.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.1

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.3.0 - 2.4.1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

If there are 100,000 records or more in the `catalog_product_option` table, the Import/Export function file validation takes longer than expected. Before Import/Export, to check option validation, Adobe Commerce loads product options for all existing products.

<u>Prerequisites</u>:

Adobe Commerce store with 5000 products with custom options. Each product should have at least four custom options with two or more options to choose from so that there are 100,000 records in `catalog_product_option` table.

<u>Steps to reproduce</u>:

1. For an **Import** example: create a CSV import file with one of the SKUs from the Commerce Admin.
1. Add four custom options to the CSV import file.
1. Try to import the CSV file from the Commerce Admin.

<u>Expected results</u>:

The Import or Export function completes as expected. Validation takes less than 10 seconds to complete with one product.

<u>Actual results</u>:

The Import or Export function takes longer than expected. Validation takes more than 10 seconds to complete with only one product.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
