---
title: 'MDVA-31295: Loyalty points on partial orders'
description: The MDVA-31295 patch fixes the issue where reward points are not calculated correctly when a partial order completes and items are taxed. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.8 is installed. Please note that the issue was fixed in Adobe Commerce 2.4.2.
exl-id: 10e8a3a9-bfab-4256-b772-fd64e8885da3
---
# MDVA-31295: Loyalty points on partial orders

The MDVA-31295 patch fixes the issue where reward points are not calculated correctly when a partial order completes and items are taxed. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.8 is installed. Please note that the issue was fixed in Adobe Commerce 2.4.2.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce on-premises 2.3.0

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.3.0 - 2.4.1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Rewards are not applied to customers' accounts when the order is complete (partially shipped) and items are taxed. When the items are not taxed, the rewards are added to the customers' accounts successfully.

<u>Steps to reproduce</u>:

1. Log in to storefront as a customer.
1. Add two products to the cart.
1. Go to checkout, set the shipping address that has tax, and place the order.
1. In the admin, go to the recently placed order.
1. Click **Invoice** and set **Qty to Invoice** to 0 for one of the items, and click **Update Qty**. Submit invoice.
1. Click Ship and set **Qty to Ship** to 0 for the item that was not invoiced. Click **Submit Shipment**.
1. Click Cancel order. The status will be set as Complete.
1. In the admin, go to **Customers** > Choose customer purchase made before > **Reward Points** > **Reward Points History**.
1. Check earned reward points for the placed order.

<u>Expected results</u>:

The reward points should be calculated for taxable orders when a partial order completes.

<u>Actual results</u>:

Reward points are not calculated for a taxable order when a partial order completes.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
