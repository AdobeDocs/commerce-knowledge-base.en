---
title: "MDVA-32133 patch: page builder doesn't load media gallery"
description: The MDVA-32133 patch solves the issue where the Media Gallery is not loaded. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.12 is installed. Please note that this issue is scheduled to be fixed in Adobe Commerce 2.4.3.
exl-id: c0ce799d-b452-4044-9635-4218db3904ef
---
# MDVA-32133 patch: page builder doesn't load media gallery

The MDVA-32133 patch solves the issue where the Media Gallery is not loaded. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.12 is installed. Please note that this issue is scheduled to be fixed in Adobe Commerce 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.4.0

**Compatible with Adobe Commerce versions:**

Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.4.0 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Fixes the issue where the order history loads very slow or not loaded at all.

<u>Steps to reproduce</u>:

1. Edit selected cms page.
1. Expand Content and click **Edit with Page Builder**.
1. Expand Media. Drag and drop Image on the Row area.
1. Click **Select from Gallery**.
1. You can log out and then log in via some other window.

<u>Expected results</u>:

The media gallery is loaded.

<u>Actual results</u>:

The media gallery is not loaded.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
