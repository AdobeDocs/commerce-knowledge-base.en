---
title: 'MDVA-36615: catalog products grid filter incorrect results'
description: The MDVA-36615 patch fixes the issue with incorrect product count in the admin product grid. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.21 is installed. The patch ID is MDVA-36615. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.3.
exl-id: 7ed70753-c637-4c13-8290-aa5e8a4d1b65
feature: Catalogs, Products
role: Admin
---
# MDVA-36615: catalog products grid filter incorrect results

The MDVA-36615 patch fixes the issue with incorrect product count in the admin product grid. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.21 is installed. The patch ID is MDVA-36615. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.4.2

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Incorrect product count in the admin product grid.

<u>Steps to reproduce:</u>

1. Create simple and configurable products with the same phrase in the name (e.g. "red shirt" / "red shirt xs").
1. On the *Admin* sidebar, go to **Catalog** > **Products** > search for this phrase.
1. Click **Filters**. Set Type to *Configurable Product*.
1. Click **Apply Filters**.

<u>Actual result:</u>

Correct number in matched product counter.

<u>Expected result:</u>

Incorrect number in matched product counter.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
