---
title: "ACSD-49849: Customer email was replaced with PayPal email"
description: Apply the ACSD-49849 patch to fix the Adobe Commerce issue where the customer email was replaced with PayPal email when placing an order with PayPal Express via GraphQL.
---
# ACSD-49849: Customer email is replaced with [!DNL PayPal] email

The ACSD-49849 patch fixes the issue where a customer's email is replaced with a [!DNL PayPal's] email when placing an order with [!DNL PayPal Express] via GraphQL. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.29 is installed. The patch ID is ACSD-49849. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5-p1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.3.7 - 2.4.5-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

A customer's email is replaced with a [!DNL PayPal's] email when placing an order with [!DNL PayPal Express] via GraphQL.

<u>Steps to reproduce</u>:

1. Go to **[!UICONTROL Configuration]** > **[!UICONTROL Sales]** > **[!UICONTROL Payments]**. 
1. Enable and configure [!DNL PayPal Express] and set **[!UICONTROL Payment Action]** = **[!UICONTROL Sale]**.
1. Go to **[!UICONTROL Catalog]** > **[!UICONTROL Products]**, and create a simple product.
1. Create a simple product.
1. Complete the guest checkout using *[!UICONTROL GraphQL]*
[GraphQL checkout tutorial](https://developer.adobe.com/commerce/webapi/graphql/tutorials/checkout/).
1. Use PayPal Express as payment method. 
1. Note the email you used on this step:
[Set email address tutorial](https://developer.adobe.com/commerce/webapi/graphql/tutorials/checkout/set-email-address/).
1. After order is placed, go to **[!UICONTROL Admin]** and check email in the created order.

<u>Expected results</u>:

Email should be the same as set during checkout.

<u>Actual results</u>:

Email set during the checkout is overridden by email set in PayPal account.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.
