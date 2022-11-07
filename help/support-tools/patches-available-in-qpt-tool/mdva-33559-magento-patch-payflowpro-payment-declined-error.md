---
title: "MDVA-33559 patch: PayflowPro payment declined error"
description: "The MDVA-33559 patch solves the issue where PayPal PayflowPro payments are declined."
---

# MDVA-33559 patch: PayflowPro payment declined error

The MDVA-33559 patch solves the issue where PayPal PayflowPro payments are declined.

This patch is available when the [Quality Patches Tool (QPT)](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching.html#mqp) 1.0.15 is installed. Please note that the issue is scheduled to be fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

 **The patch is created for Adobe Commerce version:** Adobe Commerce on cloud infrastructure 2.3.5-p2

 **Compatible with Adobe Commerce versions:** Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.0 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

The issue concerns the ampersand sign (&) and equal sign (=) special characters being used in names.

<u>Steps to reproduce</u>:

1. Add a simple product to the cart.
1. Go to checkout.
1. Set the shipping address. (Example shipping address: **First Name** = ** *John's* **  **Last Name** = ** *Apples & Oranges, Inc* **  **Street Address** = *1234 E Nameless St*  **Country** = *US*  **State/Province** = *Anystate*  **City** = *Anytown*  **Zip** = *12345*  **Phone** = *1234567890*)
1. Set payment to **PayPal PayflowPro** and attempt to complete checkout.

<u>Expected results</u>:

The transaction results in a successful payment or a correct error message, as expected.

<u>Actual results</u>:

The transaction is declined, and the customer receives an email saying, "Transaction has been Declined."

## Apply the patch

To apply individual patches, use the following links, depending on your Adobe Commerce product:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT tool, refer to the [Patches available in QPT tool](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section.