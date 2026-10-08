---
title: Google Tag Manager is broken by the [!DNL Live Search] widget
description: This article offers a solution to the [!DNL Live Search Product Listing Widget] causing [!DNL Google Tag Manager] to stop functioning.
feature: Install, Search, Best Practices
role: Admin, Developer
exl-id: 485f8ccb-cba2-4785-a8e1-a1e98c88b21e
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 6388cf7b-8a81-5248-a1e4-7bb57bbe250f
    internal-label: Install
  - id: cdfd3bc1-dc23-5cf0-b965-d3c0c55cde67
    internal-label: Best Practices
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
subfeature_v2:
  - id: a1d22079-48b9-5e69-9ee6-eb236068ef34
    internal-label: Search
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# [!DNL Google Tag Manager] is broken by the [!DNL Live Search] widget

This article offers a solution to the [!DNL Live Search Product Listing Widget] causing [!DNL Google Tag Manager] to stop functioning.

## Affected products and versions

* Adobe Commerce version 2.4.4 - 2.4.6-p2

## Issue

The [!DNL Live Search Product Listing Widget] causes [!DNL Google Tag Manager] to stop functioning.

## Solution

To ensure that [!DNL Google Tag Manager] works with [!DNL Live Search], use the *Search Adapter*. 

To do so, disable the widget in the Admin. [!DNL Live Search] then defaults to using the *Search Adapter*.

## Related reading

* [[!DNL Live Search] Guide Overview](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/guide-overview.html) in our Adobe Commerce Live Search Documentation

* [Installing [!DNL Live Search]](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/onboard/install.html) in our Adobe Commerce Live Search Documentation
