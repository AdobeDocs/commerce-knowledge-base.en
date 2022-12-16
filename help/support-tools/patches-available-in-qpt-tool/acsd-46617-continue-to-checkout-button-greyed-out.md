---
title: 'ACSD-46617: "Continue to Checkout" button greyed out when subtotal greater than "Minimum Order Amount"'
description: Apply the ACSD-46617 patch to solve the Adobe Commerce issue where the "Continue to Checkout" button is greyed out even if the subtotal is greater than the configured "Minimum Order Amount".
---
# ACSD-46617: "Continue to Checkout" button greyed out when subtotal greater than "Minimum Order Amount"

This ACSD-46617 patch solves the issue where the "Continue to Checkout" button is greyed out even if the subtotal is greater than the configured "Minimum Order Amount". This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.24 is installed. The patch ID is ACSD-46617. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.3-p1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.0 - 2.4.5-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

"Continue to Checkout" button is greyed out even if the subtotal is greater than the configured "Minimum Order Amount".

<u>Steps to reproduce</u>:

1. Enable Minimum Order Amount in Admin > **[!UICONTROL Store]** > **[!UICONTROL Configuration]** > **[!UICONTROL Sales]** > **[!UICONTROL Minimum Order Amount]**.

    * Enable: Yes
    * Minimum Amount: 2

1. Create a Cart Price Rule.

    * Coupon Code: TEST (optional)
    * Conditions: Keep empty
    * Actions:
        * Apply: Percent of product price discount
        * Discount Amount: 92
        * Apply to Shipping Amount: Yes
