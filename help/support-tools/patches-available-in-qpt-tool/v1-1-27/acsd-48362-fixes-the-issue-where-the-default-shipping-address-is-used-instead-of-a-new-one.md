---
title: 'ACSD-48362: fixes the use of default shipping address instead of a new one'
description: Apply the ACSD-48362 patch to fix the Adobe Commerce issue where the default shipping address is used instead of a new one when placing an order using a negotiable quote.
---

# ACSD-48362: fixes the use of default shipping address instead of a new one

The ACSD-48362 patch fixes the issue where the default shipping address is used instead of a new one when placing an order using a negotiable quote. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.27 is installed. The patch ID is ACSD-48362. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Magento version:**

* Adobe Commerce (all deployment methods) 2.4.4

**Compatible with Magento versions:**

* Adobe Commerce (all deployment methods) 2.4.1 - 2.4.6

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

When a customer adds a new shipping address on the negotiable quote page, the checkout page still uses the default shipping address. 

<u>Steps to reproduce</u>:

1. Enable **[!UICONTROL B2B quote]** from **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL B2B features]** > Enable company > Enable B2B quote.
1. Log in as a company user account.
1. Add a product to the cart.
1. Go to the cart page and **[!UICONTROL Request a Quote]**.
1. Go to the customer **[!UICONTROL My Quotes]** page and select the quote that was just created.
1. In the customer quote page **[!UICONTROL Shipping Information]** section, click **[!UICONTROL Add New Address]**, fill out the form, and Save Address (do not select **[!UICONTROL Use as my default billing address]** or **[!UICONTROL Use as my default shipping address]**).
1. Click **[!UICONTROL Send for Review]** on the customer quote page.
1. Under **[!UICONTROL Admin]** as an admin user open the quote that was just created and click **[!UICONTROL Send]**.
1. On the customer quote page, refresh and click **[!UICONTROL Proceed to Checkout]**.
1. On the checkout page, data shows the default shipping address even when the new shipping address is selected.
1. Continue and click **[!UICONTROL Place Order]**.

<u>Expected results</u>:
The order should use the new address without reselecting the shipping addresses on the checkout page.

<u>Actual results</u>:
The order is placed with the default shipping address.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide. 

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.