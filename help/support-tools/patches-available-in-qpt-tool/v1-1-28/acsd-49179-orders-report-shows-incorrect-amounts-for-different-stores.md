---
title: "ACSD-49179: Orders report shows incorrect amounts for different stores."
description: Apply the ACSD-49179 patch to fix the Adobe Commerce issue where the orders report shows incorrect amounts in case of different currencies for different stores.
---
# ACSD-49179: Orders report shows incorrect amounts for different stores

The ACSD-49179 patch fixes the issue where the orders report shows incorrect amounts in the case of different currencies for different stores. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.28 is installed. The patch ID is ACSD-49179. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.3-p3

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.2 - 2.4.6

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

The orders report shows incorrect amounts in the case of different currencies for different stores.

<u>Steps to reproduce</u>:

1. Go to **[!UICONTROL Stores]** > **[!UICONTROL Config]** > **[!UICONTROL Catalog]** > **[!UICONTROL Price]** and set [!UICONTROL Catalog Price Scope] = [!UICONTROL Website].
Catalog Price Scope = Website
1. Create an additional website, store, and store view.
1. Go to **[!UICONTROL Stores]** > **[!UICONTROL Config]** > **[!UICONTROL General]** > **[!UICONTROL Currency Setup]** > **[!UICONTROL Currency Options]** and set:
    * [!UICONTROL Default Config]:
    * [!UICONTROL Base Currency]: USD
    * Default Display Currency : USD
    * [!UICONTROL Allowed Currencies]: EUR, USD and THB (Thai Baht)
    * [!UICONTROL Main Website]:
    * Base Currency: EUR
    * Default Display Currency : EUR
    * Allowed Currencies: EUR
    * [!UICONTROL Additional new Website]:
    * Base Currency: THB (Thai Baht)
    * Default Display Currency : THB (Thai Baht)
    * Allowed Currencies: THB (Thai Baht)
1. Go to **[!UICONTROL Stores]** > **[!UICONTROL Currency]** > **[!UICONTROL Currency Rates]** and set the empty conversion rates for the THB (set rates to 1.0000)
1. Create a product, assign it to both websites, and place an order with this product in the additional website previously created.
1. Make sure that the order is in status Processing (invoice it)
1. In the backend, go to **[!UICONTROL Reports]** > **[!UICONTROL Sales]** > **[!UICONTROL Orders]**.
1. Click on the *[!UICONTROL Yellow]* warning to refresh the statistics
1. Set the scope of the report on the additional website previously created and set the filter as following:
    * [!UICONTROL Date Used]: [!UICONTROL Created]
    * [!UICONTROL Period]: [!UICONTROL Day]
    * From and To: the same day of when the test order was placed
    * Order Status: any
    * Empty rows: No
    * Show Actual Values: No

<u>Expected results</u>:

Sales total should show the total of the placed order, converted in the currency of the website.

<u>Actual results</u>:

The totals are zero.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.