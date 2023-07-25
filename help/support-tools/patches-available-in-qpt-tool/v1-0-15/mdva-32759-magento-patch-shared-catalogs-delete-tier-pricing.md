---
title: 'MDVA-32759 patch: shared catalogs delete tier pricing'
description: The MDVA-32759 patch solves the issue where shared catalogs delete existing tier pricing.
exl-id: c6192d2f-cd25-483e-ba69-01ca62996faf
feature: B2B, Catalogs
---
# MDVA-32759 patch: shared catalogs delete tier pricing

The MDVA-32759 patch solves the issue where shared catalogs delete existing tier pricing.

This patch is available when the [Quality Patches Tool (QPT)](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching.html#mqp) 1.0.15 is installed. Please note that the issue is scheduled to be fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.4-p2

**Compatible with Adobe Commerce versions:**

Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.0 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Prerequisites</u>:

Install Adobe Commerce with B2B, with **B2B Features** enabled.

<u>Steps to reproduce</u>:

1. Go to **Stores > Configuration > B2B Features > Enable Company** and **Shared Catalog**.
1. Run `bin/magento cron:run`.
1. Create a simple product, click on **Advanced Pricing**, and add **Catalog and Tier price**, and then save it.
1. Go to **Catalog > Shared Catalog > Set Pricing and Structure**, click on **Configure**, and from that drop-down menu, deselect all options and save.
1. Run `bin/magento cron:run`.
1. Open the above created product, and check advanced pricing.

<u>Expected results</u>:

The tier prices should not be removed from the products after removing all products from the public shared catalog, as expected.

<u>Actual results</u>:

The tier prices get removed after removing all products from the public shared catalog.


## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
