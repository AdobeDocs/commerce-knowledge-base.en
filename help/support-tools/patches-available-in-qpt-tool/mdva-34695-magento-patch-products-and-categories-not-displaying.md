---
title: 'MDVA-34695: Products and categories not displaying'
description: The MDVA-34695 patch solves the issue where products and categories don't display in the categories grid in Admin. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.18 is installed. The patch ID is MDVA-34695. Please note that the issue was fixed in Adobe Commerce version 2.4.3.
exl-id: 0c2e50c1-648b-480a-a768-72af721950d8
---
# MDVA-34695: Products and categories not displaying

The MDVA-34695 patch solves the issue where products and categories don't display in the categories grid in Admin. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.18 is installed. The patch ID is MDVA-34695. Please note that the issue was fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.4

**Compatible with Adobe Commerce versions:**

Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure 2.3.0-2.4.0-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Negative values for `children_count` appear in the database after deleting categories.

<u>Steps to reproduce</u>:

1. Log in to the Admin backend.
1. Navigate to **Catalog > Categories**.
1. Click **Add Subcategory**.
1. Set **category name** = *Parent 1*, then Save.
1. Click **Add Subcategory**.
1. Set **category name** = *Child 1*, then Save.
1. Click **Add Subcategory**.
1. Set **category name** = *Child 2*, then Save.
1. Click **Add Subcategory**.
1. Set **category name** = *Child 3*, then Save. At this point, this category should have a level = *5*.
1. Click on the **Child 1** category.
1. Delete the category.

<u>Expected results</u>:

The categories grid shows products and categories, as expected.

<u>Actual results</u>:

The categories grid is empty. Check the `catalog_category_entity` table in the database. Note that `children_count` became negative.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section.
