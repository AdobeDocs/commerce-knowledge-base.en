---
title: Live Search displays out-of-stock products regardless of stock status settings in admin
description: This article provides information on the known issue where the Product Listing Page (PLP) shows the *We can’t find products matching the selection* error while the search popover returns some items.
exl-id: 2a351b83-407c-444a-a761-4932b5b88843
---
# [!DNL Live Search] displays out-of-stock products regardless of stock status settings in admin

>[!IMPORTANT]
>
>This issue was fixed in [[!DNL Live Search] [2.0.4]](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/release-notes.html?lang=en). To install the latest version, refer to [Updating [!DNL Live Search]](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/onboard/install.html?lang=en#update) in the user guide.

This article provides information on the known issue where the Product Listing Page (PLP) shows the *We can’t find products matching the selection* error while the search popover returns some items.

## Affected products and versions

Adobe Commerce (all deployment methods) 2.4.x

## Issue

[!DNL Live Search] displays search results regardless of the stock status settings in the Adobe Commerce Admin. Even when the **[!UICONTROL Display Out-of-Stock Products]** is set to *No*, the products are displayed. It results in the PLP error *We can’t find products matching the selection*.

<u>Steps to reproduce</u>:

1. Create a category, add products. (Example: Category = _Jeans_, Product1 = _Blue Jeans_, Product2 = _Black Jeans_)
1. Make all products in the category out of stock.
1. Set **[!UICONTROL Display Out-of-Stock Products]** to *No*.
1. On the storefront, enter *Jeans* in the search field.
1. Click **[!UICONTROL View All]** in the pop-up.

<u>Expected result</u>:

You see the *We can’t find products matching the selection* message on PLP, and no products are displayed on the search pop-up.

<u>Actual result</u>:

You see the *We can’t find products matching the selection* message on PLP, and both products are displayed on the search pop-up.

## Solution

There is no solution for this issue at the moment. Our [!DNL Live Search] team will soon provide a setting to configure [!DNL Live Search] to display products correctly.

## Related reading

[Install [!DNL Live Search]](https://docs.magento.com/user-guide/live-search/install.html) in our user guide.
