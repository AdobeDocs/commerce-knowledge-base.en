---
title: 'MDVA-33482 patch: tax miscalculation in credit memo'
description: The MDVA-33482 patch solves the issue where tax is miscalculated in credit memos.
exl-id: 80740e6f-2b6c-4770-9a1a-58ba68a1b28f
---
# MDVA-33482 patch: tax miscalculation in credit memo

The MDVA-33482 patch solves the issue where tax is miscalculated in credit memos when there is no Adjustment Fee or Adjustment Refund applied.

This patch is available when the [Quality Patches Tool (QPT)](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching.html#mqp) 1.0.15 is installed. Please note that the issue is scheduled to be fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:** Adobe Commerce on cloud infrastructure 2.4.0

**Compatible with Adobe Commerce versions:** Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.5 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Steps to reproduce</u>:

1. Configure **Taxes**.
1. Create an order using two products in the backend using any online payment method (Example: [!DNL PayPal Payment Pro]). Make sure that taxes are applied to all the products.
1. Create two invoices for the order.
1. Create a credit memo against one of the invoices. STOP if you intend to apply an Adjustment Fee or Adjustment Refund - the fix does not apply to this scenario.
1. Check the credit memo totals.

<u>Expected results</u>:

Only a partially-invoiced tax amount is in the credit memo, as expected.

<u>Actual results</u>:

The full tax amount is displayed in the credit memo.

## Apply the patch

To apply individual patches, use the following links, depending on your Adobe Commerce product:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT tool, refer to the [Patches available in QPT tool](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section.
