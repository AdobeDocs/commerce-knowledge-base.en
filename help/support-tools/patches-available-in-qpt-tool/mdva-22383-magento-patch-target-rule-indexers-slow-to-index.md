---
title: "MDVA-22383: target rule indexers slow to index"
description: "The MDVA-22383 patch solves the issue where reindexing the Product/Target Rule and Target Rule/Product indexers is taking too long. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.20 is installed. The patch ID is MDVA-22383. Please note that the issue was fixed in Adobe Commerce 2.3.5."
---

# MDVA-22383: target rule indexers slow to index

The MDVA-22383 patch solves the issue where reindexing the Product/Target Rule and Target Rule/Product indexers is taking too long. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.20 is installed. The patch ID is MDVA-22383. Please note that the issue was fixed in Adobe Commerce 2.3.5.

## Affected products and versions

 **The patch is created for Adobe Commerce version:** Adobe Commerce on cloud infrastructure 2.3.2

 **Compatible with Adobe Commerce versions:** Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.0-2.3.3-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Reindexing the Product/Target Rule and Target Rule/Product indexers is taking too long.

 <u>Prerequisites:</u> the issue happens when there is a large number of products.

 <u>Steps to reproduce:</u>

1. Create a target rule with products to match the conditions, the conditions should add more product to collection and should have attributes (not categories or attribute set).
1. Run the following command:

   ```bash
       bin/magento indexer:reindex targetrule_product_rule
   ```

 <u>Actual result:</u>

Reindexing is stuck; product saving is stuck.

 <u>Expected result:</u>

Reindexing is completed successfully.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-MQP-tool-) section.