---
title: 'MDVA-38308: Error after adding Vimeo videos to disabled products'
description: 'The MDVA-38308 quality patch for Adobe Commerce solves the issue where users get the error message: *Notice: Undefined index: extension in /lib/internal/Magento/Framework/File/Uploader.php on line 806,* when adding Vimeo videos to disabled products. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.26 is installed. The patch ID is MDVA-38308. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.4.'
exl-id: ed5fb9ec-c465-4bb9-8a29-4d5e4bd4c867
---
# MDVA-38308: Error after adding Vimeo videos to disabled products

The MDVA-38308 quality patch for Adobe Commerce solves the issue where users get the error message: *Notice: Undefined index: extension in /lib/internal/Magento/Framework/File/Uploader.php on line 806,* when adding Vimeo videos to disabled products. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.26 is installed. The patch ID is MDVA-38308. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.4.

## Affected products and versions

**The patch is created for Adobe Commerce version:**
Adobe Commerce on cloud infrastructure 2.4.1-p1, 2.4.2-p1

**Compatible with Adobe Commerce versions:**
Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure 2.3.5 - 2.3.6-p1, 2.4.0 - 2.4.1-p1, 2.4.2 - 2.4.2-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

When adding Vimeo videos to disabled products, you receive the following error message:  *Notice: Undefined index: extension in /lib/internal/Magento/Framework/File/Uploader.php on line 806*

<u>Steps to reproduce</u>:

1. Create a simple product.
1. Disable the created product.
1. Try to add a Vimeo video to the disabled product.

<u>Expected results</u>:

Video is added without any error.

<u>Actual results</u>:

You get the following error:
*Notice: Undefined index: extension in /lib/internal/Magento/Framework/File/Uploader.php on line 806*

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html)
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html)

## Related reading

To learn more about Quality Patches Tool in our support knowledge base, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md)
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md)

For info about other patches available in QPT tool, refer to the [Patches available in QPT tool](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section in our support knowledge base.
