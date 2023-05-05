---
title: 'MDVA-35356: Wrong store credit return after canceling partially invoiced order'
description: The MDVA-35356 patch fixes the issue with incorrect store credit return after partially invoiced order cancellation. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-35356. Please note that the issue was fixed in Adobe Commerce version 2.4.3.
exl-id: af37f318-0818-4393-b768-939f08b73847
---
# MDVA-35356: Wrong store credit return after canceling partially invoiced order

The MDVA-35356 patch fixes the issue with incorrect store credit return after partially invoiced order cancellation. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-35356. Please note that the issue was fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.4.1

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.3.0-2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Steps to reproduce</u>:

1. Create three simple products.
1. Create a new user and assign store credit (Example: store credit = *$10,* simple product prices = *$100*, *$200*, and *$300*).
1. Log in with the above user, and add the three products to the cart.
1. Check out the three products in the cart, and utilize the store credit for a portion of the order (Example: paid with **Check/Money order**).
1. Perform two invoices on the order through the API, one for Product 1 and one for Product 2:

    ```php
    //endpoint POST {\{baseUrl}}/V1/order/:orderId/invoice    //1st API call:    {    "capture": true,    "items": [    {    "order_item_id": 1,    "qty": 1    }    ],    "notify": true,    "appendComment": false    }    //2nd API call:    {    "capture": true,    "items": [    {    "order_item_id": 2,    "qty": 1    }    ],    "notify": true,    "appendComment": false    }
    ```

1. Notice that the store credit is fully applied to the first invoice.
1. ​Notice that the store credit balance = *0*.
1. Cancel the order, and see that two items are invoiced and that the third item is canceled.
1. Observe the store credit balance.

<u>Expected results</u>:

The store credit balance is still 0 because the $10 store credit has been invoiced.

<u>Actual results</u>:

The full store credit is returned: the balance is $10.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
