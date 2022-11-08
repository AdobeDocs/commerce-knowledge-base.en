---
title: 'MDVA-36424: Images attached to page builder vanish on save'
description: The MDVA-36424 patch solves the issue where the images attached to page builder elements disappear when the category is saved for the second time in the case of multiple websites, with the default website's base URL being different from the admin URL. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.21 is installed. The patch ID is MDVA-36424. Please note that the issue was fixed in Adobe Commerce 2.4.3.
exl-id: ae15db2d-0d9f-48c1-87e4-61da1558a57c
---
# MDVA-36424: Images attached to page builder vanish on save

The MDVA-36424 patch solves the issue where the images attached to page builder elements disappear when the category is saved for the second time in the case of multiple websites, with the default website's base URL being different from the admin URL. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.21 is installed. The patch ID is MDVA-36424. Please note that the issue was fixed in Adobe Commerce 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.6

**Compatible with Magento versions:**

Adobe Commerce (all deployment methods) 2.3.5 - 2.4.1-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Media images attached to page builder elements are not saved if the backend base URL is different from the storefront base URL.

<u>Steps to reproduce</u>:

1. Create a second website - website2.
1. Set a different base URL for website2 (the base URL used in admin should be different from the second website).
1. Set the second website as the default website (**Stores** > *Settings* > **All Stores** > Select the second website > set as *Default*).
1. Navigate to the category page in the backend, go to a category edit view.
1. Navigate to **Content** > *Description*.
1. Add a column to the content and set a background image using the media gallery.
1. Save the category.
1. Go to the **Content** > *Description* again; you will see the saved image correctly.
1. Save the category again.
1. Go to the **Content** > *Description*.

<u>Expected results</u>:

The image is not removed when saving the category.

<u>Actual results</u>:

The image is removed after saving the category a second time.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
