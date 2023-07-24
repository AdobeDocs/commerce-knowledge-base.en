---
title: 'MDVA-36718: Custom options remain after API change'
description: The MDVA-36718 Magento patch fixes the issue when the old custom options remain after being changed via API.
exl-id: e9755764-e563-4921-af75-a90e06237053
feature: REST
---
# MDVA-36718: Custom options remain after API change

The MDVA-36718 Magento patch fixes the issue when the old custom options remain after being changed via API.

This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.22 is installed. The patch ID is MDVA-36718. Please note that the issue is scheduled to be fixed in Magento version 2.4.3.

## Affected products and versions

 **The patch is created for Adobe Commerce version:**

 Adobe Commerce on cloud infrastructure 2.4.1

 **Compatible with Magento versions:**

 Adobe Commerce (all deployment methods) 2.3.0-2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

 <u>Steps to reproduce</u>:

1. Create a simple product.
1. Add a **drop-down type** custom option.
1. Update the custom option via API: Send `PUT` request to `/V1/products/options/{optionId}`.

 <u>Expected results</u>:

The custom options are updated, as expected.

 <u>Actual results</u>:

New custom options are added, but the old custom options remain.

## Apply the patch

o apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check patch for Magento issue with Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT tool, refer to the [Patches available in QPT tool](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section.
