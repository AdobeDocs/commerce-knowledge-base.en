---
title: Checkout is stuck when Authorize.net payment method is used
description: This article provides an explanation and fix for the Adobe Commerce 2.3.X issue where the checkout gets stuck if Authorize.net is used, with the *'Cannot read property 'length' of null'* error message in the browser console log.
exl-id: 01dc1147-4010-4dc5-81f3-3b3015a8c47c
feature: Cache, Checkout, Console, Orders, Payments
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 8cd50456-5eb0-5364-922a-f14161feb828
    internal-label: Checkout
  - id: 4820f335-ec9f-5611-8fe3-f5b7e3e56967
    internal-label: Orders
  - id: 3dcbfa9e-51f8-569c-a0e4-7f59098f730f
    internal-label: Payments
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
  - id: 125c1f49-aefd-5f34-a252-288937f95f6b
    internal-label: Marketing Tools
subfeature_v2:
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
  - id: c4af0798-d497-5e6b-8380-19812c26d00a
    internal-label: Console
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Checkout is stuck when Authorize.net payment method is used

This article provides an explanation and fix for the Adobe Commerce 2.3.X issue where the checkout gets stuck if Authorize.net is used, with the *'Cannot read property 'length' of null'* error message in the browser console log.

## Affected products and versions

* Adobe Commerce 2.3.X

>[!NOTE]
>
>The core Adobe Commerce Authorize.Net payment integration has been deprecated since 2.3.4 and was completely removed in 2.4.0. Use an extension that suits your needs from the [Adobe Commerce [!DNL Marketplace]](https://commercemarketplace.adobe.com/) instead.

## Issue

 <u>Steps to reproduce</u>

1. Configure the Authorize.net payment method in the Commerce Admin.
1. Go to the storefront.
1. Add a product to the cart and proceed to checkout.
1. Choose Authorize.net as a payment method.
1. Click **Place Order**.

 <u>Expected result</u>

The Authorize.net iframe is loaded.

 <u>Actual result</u>

Ajax spinner is displayed, and the page never loads. The following JS error is displayed in the browser console log: *'Uncaught TypeError: Cannot read property 'length' of null at b (jstest.authorize.net/v1/AcceptCore.js:1)'*

## Cause

One of the most common reasons for this issue is the Public Client Key not being specified in the Authorize.Net configuration in the Commerce Admin.

## Solution

Under **Stores** > **Settings** > **Configuration** > **Sales** > **Payment Methods**, in the **Authorize.net** section, check if the value is specified in the **Public Client Key** field. If it is empty, enter the key value from your Authorize.Net merchant account.

For the changes to be applied, clean the cache by running

```bash
bin/magento cache:clean
```
