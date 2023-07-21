---
title: 'MDVA-33289 patch: Javascript in address at checkout'
description: The MDVA-33289 patch fixes the problem where Javascript shows in address at payment. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-33289. Please note that the issue was scheduled to be fixed in Adobe Commerce 2.4.3.
exl-id: 247e4f05-7e89-4d37-b3d4-c2cae7595267
feature: Checkout, Marketing Tools
---
# MDVA-33289 patch: Javascript in address at checkout

The MDVA-33289 patch fixes the problem where Javascript shows in address at payment. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-33289. Please note that the issue was scheduled to be fixed in Adobe Commerce 2.4.3.

## Affected products and versions

 **The patch is created for Adobe Commerce version:** Adobe Commerce on cloud infrastructure 2.4.1

 **Compatible with Adobe Commerce versions:** Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.4.0 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

When checking out with Google Tag Manager (GTM) enabled, Javascript shows in the address field.

<u>Steps to reproduce</u>:

1. Enable GTM. See [Google Tag Manager](https://docs.magento.com/user-guide/marketing/google-tag-manager.html) in our user guide, for details.
1. In the storefront, add some products to the cart.
1. Check out.

<u>Actual result</u>:

The address section updates, but includes a lot of Javascript code text.

<u>Expected result</u>:

Address is shown.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
