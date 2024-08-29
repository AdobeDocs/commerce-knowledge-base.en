---
title: 'ACSD-57086: Orders from non-default websites with terms and conditions enabled are processed incorrectly'
description: Apply the ACSD-57086 patch to fix the Adobe Commerce issue where orders placed from non-default websites with terms and conditions enabled are not processed correctly.
feature: Orders
role: Admin, Developer
---

# ACSD-57086: Orders from non-default websites with terms and conditions enabled are processed incorrectly

The ACSD-57086 patch fixes the issue where orders placed from non-default websites with terms and conditions enabled are not processed correctly. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.49 is installed. The patch ID is ACSD-57086. Please note that this issue was fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.7

**Compatible with Adobe Commerce and Magento Open Source versions:**

* Adobe Commerce (all deployment methods) 2.4.3 - 2.4.6-p7

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

While using a multi-store setup with Async order processing, orders placed on any websites/stores other than the main website, are rejected due to issues with scope handling on the queue consumer code.

<u>Steps to reproduce</u>:

1. Install [!DNL RabbitMQ] and execute `bin/magento setup:upgrade` to create the queues for [!DNL RabbitMQ].
1. Configure Async order processing with:

    ```bash
    bin/magento setup:config:set --checkout-async 1
    ```

1. Create a secondary website, a store, and a store view.
1. Create a product that is shared between both websites.
1. Enable terms and conditions:
    * Go to **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Sales]** > **[!UICONTROL Checkout]** > **[!UICONTROL Checkout]** > **[!UICONTROL Options]** > **[!UICONTROL Enable Terms And Conditions]** > **[!UICONTROL Yes]**
1. Configure terms and conditions for both the websites:
    * Go to **[!UICONTROL Stores]** > **[!UICONTROL Terms And Conditions]** > **[!UICONTROL Add new Condition]**
    * Use the following settings:

    ```json
    {
        "Condition Name": "anything",
        "Status": "Enabled",
        "Applied": "Manually",
        "Store View": "Default Store View"
    }
    ```

    * Create another condition for the second website/store view.
1. Change the default website by going to **[!UICONTROL Stores]** > **[!UICONTROL All Stores]**. Click the second website, check *[!UICONTROL Set as Default]* and save.
1. Clear the cache with:

    ```bash
    bin/magento cache:clear
    ```

1. Go to the frontend and add a product to the cart. Proceed to checkout and place an order (you should see a checkbox in the payment method step to accept the terms and conditions).
1. Go back to Admin after placing the order, and change the default website back to the original main website and save.
1. Clear the cache:

    ```bash
    bin/magento cache:clear
    ```

1. Run the following command to start the queue consumer:

    ```bash
    bin/magento queue:cons:start placeOrderProcessor
    ```

<u>Expected results</u>:

Order is fulfilled; it is not automatically rejected.

<u>Actual results</u>:

Order status is *rejected* with the following comment: 

*The order wasn't placed. First, agree to the terms and conditions, then try placing your order again.* 

(Log in as Admin and check **[!UICONTROL Sales]** > **[!UICONTROL Orders]**)

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [[!DNL Quality Patches Tool]: Search for patches](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.
