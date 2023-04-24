---
title: 'MDVA-31224 patch: Product price reindex takes too long'
description: The MDVA-31224 patch solves the issue when product price reindex takes too long to complete or never completes. This patch is available when the [Quality Patches Tool (QPT)](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching.html#mqp) v.1.0.7 is installed.
exl-id: 17f83fbf-9a43-4a65-b560-5f729b037c17
---
# MDVA-31224 patch: Product price reindex takes too long

The MDVA-31224 patch solves the issue when product price reindex takes too long to complete or never completes. This patch is available when the [Quality Patches Tool (QPT)](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching.html#mqp) v.1.0.7 is installed.

## Affected products and versions

* The patch was designed for Adobe Commerce on cloud infrastructure 2.3.3.
* The patch is also compatible with Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure 2.3.3 - 2.3.4-p2.

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Product price reindex takes too long to complete or never completes.

 <u>Steps to reproduce:</u>

1. Create 6000 bundled products with 15 options.
1. Create 1 bundled product with 30 options.
1. Run price reindex from CLI:     `bin/magento indexer:reindex catalog_product_price`

 <u>Expected results:</u>

Product price reindex takes 1.5 hours or more to complete.

 <u>Actual results:</u>

Product price reindex takes a short time (a minute or two) to complete.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
