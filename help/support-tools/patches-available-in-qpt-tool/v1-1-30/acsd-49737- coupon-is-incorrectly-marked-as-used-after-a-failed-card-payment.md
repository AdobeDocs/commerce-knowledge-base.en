---
title: 'ACSD-49737: Coupon is incorrectly marked as used after a failed card payment'
description: Apply the ACSD-49737 patch to fix the Adobe Commerce issue where the coupon is incorrectly marked as used after a failed card payment.
---
# ACSD-49737: Coupon is incorrectly marked as used after a failed card payment

The ACSD-49737 patch fixes the issue where the coupon is incorrectly marked as used after a failed card payment. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.30 is installed. The patch ID is ACSD-49737. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.4

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.1-p1 - 2.4.6

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Coupon is incorrectly marked as used after a failed card payment.

Configure **[!UICONTROL Braintree sandbox payment]** method.

<u>Steps to reproduce</u>:

1. Create a **[!UICONTROL Cart Price Rule]** with auto generated coupon codes. 
1. Login as a customer.
1. Add product(s) to cart.
1. Apply an **[!UICONTROL auto generated coupon code]**.
1. Try to place the order with a failed payment.
1. Execute **[!DNL bin/magento cron:run] command, which will start the **[!UICONTROL "sales.rule.update.coupon.usage]** to the consumer.
1. Check the coupon usage in the Cart Price Rule under **[!UICONTROL Manage Coupon Codes]** tab.

<u>Expected results</u>:

Coupon shouldn't be flagged as "used" if the payment is failed.

<u>Actual results</u>:

1. Coupon code says used: Yes, Times Used: 1
1. Coupon code cannot be applied again, since it's for a single time use.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Additional steps required after the patch installation

(This section is optional; there might be some steps required after applying the patch to fix the issue.) 

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [[!DNL Quality Patches Tool]: Search for patches](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.