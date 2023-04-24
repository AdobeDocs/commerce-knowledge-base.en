---
title: 'MDVA-21095: INSERT INTO "search_tmp..." never ends after mass attribute update'
description: The MDVA-21095 patch fixes the issue when a query `INSERT INTO` "search\_tmp..." never ends after a mass attribute update. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.20 is installed. The patch ID is MDVA-21095. Please note that there is no current plan to fix this issue in future versions.
exl-id: fd599473-b49a-4f9c-a13f-612d05e43f09
---
# MDVA-21095: INSERT INTO "search_tmp..." never ends after mass attribute update

The MDVA-21095 patch fixes the issue when a query `INSERT INTO` "search\_tmp..." never ends after a mass attribute update. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.20 is installed. The patch ID is MDVA-21095. Please note that there is no current plan to fix this issue in future versions.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.2

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.3.0 - 2.3.4-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

`INSERT INTO` "search\_tmp..." never ends after a mass attribute update.

<u>Step to reproduce</u>:

Perform a mass attribute values update with ~30,000 items.

<u>Expected results</u>:

The reindex process completes normally, as expected.

<u>Actual results</u>:

The reindex process completes, but a lot of queries `INSERT INTO` “search\_tmp…” start until the server reaches the `pm.max_children` parameter value and PHP-fpm dies, and these constantly reoccur even after MySQL restart and process kill.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
