---
title: 'MDVA-37913: Product download links vanish after updating extension attributes via API'
description: The MDVA-37913 patch for solves the issue where the downloadable product links disappear after updating extension attributes via API. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.24 is installed. The patch ID is MDVA-37913. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.3.
exl-id: e4b2cf59-5c35-4a28-a63e-15cd7d0d5a5d
feature: REST, Attributes, Extensions
---
# MDVA-37913: Product download links vanish after updating extension attributes via API

The MDVA-37913 patch for solves the issue where the downloadable product links disappear after updating extension attributes via API. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.24 is installed. The patch ID is MDVA-37913. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.3.


## Affected products and versions

**The patch is created for Adobe Commerce version:**
Adobe Commerce on cloud infrastructure 2.3.6

**Compatible with Adobe Commerce versions:**
Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure 2.3.0 - 2.4.0-p1
>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.


## Issue

Downloadable product links disappear after updating extension attributes via API.

<u>Prerequisites</u>:
Downloadable product with download links.

<u>Steps to reproduce</u>:

1. Update extension attributes, using request like this:

```JSON
{
    "product": {
        "extension_attributes": {
            "stock_item": {
                "is_in_stock": true,
                "qty": 100
            }
        }
    }
}
```

<u>Expected results</u>:<br>
Product is updated, all download links are not removed.

<u>Actual results</u>:<br>
Product updated, but all download links were removed.


## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html)
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html)

## Related reading

To learn more about Quality Patches Tool in our support knowledge base, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md)
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md)

For info about other patches available in QPT tool, refer to the [Patches available in QPT tool](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section in our support knowledge base.
