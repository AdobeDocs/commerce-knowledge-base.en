---
title: 'MDVA-35286: error switching Multiple Address to Onepage checkout'
description: The MDVA-35286 patch fixes the issue where there is an error if a customer has bundle products in the cart and switches from Multiple Address checkout to Onepage checkout. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.18 is installed. The patch ID is MDVA-35286. Please note that the issue was fixed in Adobe Commerce 2.4.2.
exl-id: 40c98735-6054-4b25-9882-e274424b203f
feature: "Checkout, Orders, Shipping/Delivery"
role: Admin
---
# MDVA-35286: error switching Multiple Address to Onepage checkout

The MDVA-35286 patch fixes the issue where there is an error if a customer has bundle products in the cart and switches from Multiple Address checkout to Onepage checkout. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.18 is installed. The patch ID is MDVA-35286. Please note that the issue was fixed in Adobe Commerce 2.4.2.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.4.1

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.4.0-2.4.1-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

An error is displayed if there's a bundle product in the cart and the user attempts to use Onepage Checkout after abandoning Multi-Shipping Checkout.

<u>Steps to reproduce</u>:

1. Log in to the customer account and add more than one bundle product to the cart.
1. Click the link to view and edit the cart.
1. Click the **Check Out with Multiple Addresses** link.
1. Select different addresses for products added to the cart.
1. Click **Back to Shopping Cart**.
1. In the cart, click **Proceed to Checkout**.

<u>Expected results</u>:

You get redirected to the Checkout page.

<u>Actual results</u>:

The error message is displayed: *There has been an error processing your request*.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
