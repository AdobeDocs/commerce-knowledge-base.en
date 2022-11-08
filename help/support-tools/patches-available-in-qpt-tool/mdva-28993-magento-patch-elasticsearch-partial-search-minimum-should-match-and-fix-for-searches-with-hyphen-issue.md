---
title: 'MDVA-28993: Elasticsearch partial search, "minimum should match" and fix for "searches with hyphen" issue'
description: "The MDVA-28993 patch implements the \"Minimum should match\" functionality and partial search for Elasticsearch engine, and solves issues with hyphens in search queries. The patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) v.1.0.6 is installed."
---

# MDVA-28993: Elasticsearch partial search, "minimum should match" and fix for "searches with hyphen" issue

The MDVA-28993 patch implements the "Minimum should match" functionality and partial search for Elasticsearch engine, and solves issues with hyphens in search queries. The patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) v.1.0.6 is installed.

## Affected products and versions

 **The patch is created for Adobe Commerce version:** Adobe Commerce on cloud infrastructure 2.3.4

 **Compatible with Adobe Commerce versions:** Adobe Commerce on-premises/ Adobe Commerce on cloud infrastructure 2.3.4-2.3.5-p2

 >[!NOTE]
 >
 >The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.


## Issue

When using Elasticsearch 6 for searching SKU that contains a hyphen(-), search returns too many results.

 <u>Steps to reproduce:</u>

1. Go to the storefront.

1. In the search bar enter a string containing a hyphen, for example "WS-M-Blue".

 <u>Expected result:</u>

Returns only WS-M-Blue.

 <u>Actual result:</u>

Returns all SKUs starting with "WS".

## Patch details

The MDVA-28993 patch contains the following fixes and improvements:

* implements the new "Minimum should match" functionality and partial search for Elasticsearch engine. For configuration details refer to [Configuring Catalog Search](https://docs.magento.com/user-guide/catalog/search-configuration.html#step-4-configure-minimum-terms-to-match) in our user guide.
* partial search for Elasticsearch
* fixes the "searches with hyphen" issue described above.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-MQP-tool-) section.