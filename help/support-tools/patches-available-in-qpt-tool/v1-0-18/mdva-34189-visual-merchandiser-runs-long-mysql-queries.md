---
title: 'MDVA-34189: Visual merchandiser runs long MySQL queries'
description: The MDVA-34189 patch solves the issue where Adobe Commerce executes large Visual Merchandiser queries when loading the Admin category page.
exl-id: 94143d80-3240-4a18-890d-fb759ea9c30d
feature: Categories
---
# MDVA-34189: Visual merchandiser runs long MySQL queries

The MDVA-34189 patch solves the issue where Adobe Commerce executes large Visual Merchandiser queries when loading the Admin category page.

This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.18 is installed. The patch ID is MDVA-34189. Please note that the issue is scheduled to be fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

 **The patch is created for Adobe Commerce version:** Adobe Commerce on cloud infrastructure 2.3.5-p2

 **Compatible with Adobe Commerce versions:** Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure 2.3.4-2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Website runs large MySQL queries on the Production server.

<u>Steps to reproduce</u>:

1. To access the Visual Merchandiser go to the *Admin* sidebar, click **Catalog** > **Categories**.
1. Load the **Categories** page in the Admin panel (the initial root category load) and observe the queries that it executes.

<u>Expected result</u>:

The Admin **Categories** page should load without generating slow queries.

<u>Actual result</u>:

This depends on your PHP configuration. The most common example of this error is that the **Categories** page does not open and an error *Error 503 first byte timeout* displays.

Alternately when Adobe Commerce loads the Visual Merchandiser, it executes a slow MySQL query. This query includes many product IDs inserted in to `ORDER BY FIELD(`e`.`entity_id`,  ...)`

in `app/code/Magento/VisualMerchandiser/Model/Category/Products.php:: applyPositions`

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT tool, refer to the [Patches available in QPT](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section.
