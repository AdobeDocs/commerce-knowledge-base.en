---
title: 'MDVA-36138: free shipping rule not applied cart multiple items'
description: The MDVA-36138 patch fixes the issue where when there are multiple items in the cart, the matching SKU in the Free Shipping is not getting free shipping applied to it. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.21 is installed. The patch ID is MDVA-36138. Please note that the issue was fixed in Adobe Commerce 2.4.3.
exl-id: 74e25ca8-e4fa-47f4-ab95-561f70e05727
---
# MDVA-36138: free shipping rule not applied cart multiple items

The MDVA-36138 patch fixes the issue where when there are multiple items in the cart, the matching SKU in the Free Shipping is not getting free shipping applied to it. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.21 is installed. The patch ID is MDVA-36138. Please note that the issue was fixed in Adobe Commerce 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.4

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.3.2 and above

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

If a free shipping rule is applied to only specific items, the discount doesn't apply when there are other items in the cart.

<u>Steps to reproduce</u>:

1. Create simple products - simple1 and simple2.
1. Configure USPS (or any online shipping method):

    * Allowed Methods: Priority Mail (one method selected for the purpose of not having a long list of methods in cart and checkout).
    * Free Method: Priority Mail.

1. Create a shopping cart rule:

    * Specify coupon code
    * Conditions tab: leave empty
    * Actions tab:

    `Condition: SKU is simple1`
    `Free Shipping: For matching items only`

1. Add simple1 to the cart.
1. Apply the coupon code.
1. Add simple2 to the cart.

<u>Expected results</u>:

* simple1 - should have free shipping.
* simple2 - shipping should be paid.

<u>Actual results</u>:

The shipping price includes simple1 and simple2.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
