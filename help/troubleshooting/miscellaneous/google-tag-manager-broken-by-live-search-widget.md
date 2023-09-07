---
title: Google Tag Manager is broken by the Live Search widget
description: This article offers a solution to the [!DNL Live Search Product Listing Widget] causing [!DNL Google Tag Manager] to stop functioning.
feature: Install, Search, Best Practices
role: Admin, Developer
---
# [!DNL Google Tag Manager] is broken by the Live Search widget

This article offers a solution to the [!DNL Live Search Product Listing Widget] causing [!DNL Google Tag Manager] to stop functioning.

## Affected products and versions

* Adobe Commerce (all versions)

## Issue

The [!DNL Live Search Product Listing Widget] causes [!DNL Google Tag Manager] to stop functioning.

## Solution

To ensure that  [!DNL Google Tag Manager] will work with[!DNL Live Search] , the *Search Adapter* must be used. 

To do so, disable the widget in the Admin. [!DNL Live Search] then defaults to using the Search Adapter.

>[!NOTE]
>
>You would have to [enable the widget](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/live-search-storefront/plp-styling.html) from Admin if you wish to use it, but then [!DNL Google Tag Manager] won't work properly. This is why using the default *Search Adapter* is recommended.

## Related reading

* [Live Search Guide Overview](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/guide-overview.html) in our Adobe Commerce Live Search Documentation

* [Installing Live Search](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/onboard/install.html) in our Adobe Commerce Live Search Documentation
