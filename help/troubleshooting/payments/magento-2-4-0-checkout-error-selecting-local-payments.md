---
title: 'Adobe Commerce 2.4.0: Checkout error selecting local payments'
description: 'This article talks about a solution for a known issue in Adobe Commerce during checkout where an error message appears when selecting a local payment method for some countries. This occurs for the countries: Belgium, Italy, Netherlands, Poland, and Spain.'
exl-id: de2eafb0-d03c-4ff8-9615-0f2676d95848
feature: B2B, Categories, Checkout, Orders, Payments
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
  - id: bd989d82-1e15-4534-88db-f1f51dd77ffa
    internal-label: Accounts
  - id: c18ed297-2187-4aec-affb-9d9654eca6fc
    internal-label: Catalog management
subfeature_v2:
  - id: f56d26ed-050b-4fb7-b29b-8e6e994e80a2
    internal-label: B2B
  - id: e91a50b1-0b31-436e-9033-00e4776e94cb
    internal-label: Categories
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce 2.4.0: Checkout error selecting local payments

This article talks about a solution for a known issue in Adobe Commerce during checkout where an error message appears when selecting a local payment method for some countries. This occurs for the countries: Belgium, Italy, Netherlands, Poland, and Spain.

The error message, "*There are currently no available payment methods. Please update your Billing Address.*" will appear, but the local payment methods will still appear and function correctly. A permanent fix will be available in Adobe Commerce 2.4.1.

## Affected products and versions

* Adobe Commerce on-premises 2.4.0
* Adobe Commerce on cloud infrastructure 2.4.0

## Issue

<u>Prerequisites</u>:

* Adobe Commerce 2.4.0 is installed.
* Create one product and one category.
* Configure [Braintree Payment Method](https://developer.adobe.com/commerce/webapi/graphql/payment-methods/braintree/).

<u>Steps to reproduce</u>:

1. Navigate to the storefront.
1. Select items to add to the cart.
1. Proceed to checkout.
1. Fill out the address form with a valid address.
1. Proceed to the Review & Payments page.

<u>Expected result</u>:

The local payment methods should be displayed normally, without an error message.

<u>Actual result</u>:

The error message, "*There are currently no available payment methods. Please update your Billing Address.*" appears, but the local payment methods will still display and function correctly.

## Solution

The solution is to ignore the displayed error message and continue with payment as normal, as all local payment methods will function normally. The fix was available starting with Adobe Commerce version 2.4.1.

## Related reading

* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2-4-0-braintree-not-in-multiple-addresses-checkout.md)
