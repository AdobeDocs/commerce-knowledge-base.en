---
title: 'Adobe Commerce 2.4.0: Braintree not in Multiple Addresses checkout'
description: This article provides a workaround for an Adobe Commerce 2.4.0 known issue where Braintree payment methods are not included in working with Multiple Addresses checkout. Please note that the issue was fixed in Adobe Commerce 2.4.1.
exl-id: efde0bba-fd4a-490b-becb-856cb9ea58a5
feature: Checkout, Compliance, Orders, Payments, Shipping/Delivery
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 8cd50456-5eb0-5364-922a-f14161feb828
    internal-label: Checkout
  - id: b5f00040-57a0-4a6d-a39e-383b1936c2c9
    internal-label: Compliance
  - id: 4820f335-ec9f-5611-8fe3-f5b7e3e56967
    internal-label: Orders
  - id: 3dcbfa9e-51f8-569c-a0e4-7f59098f730f
    internal-label: Payments
  - id: 04d3134c-2afb-5bd7-ac14-e19fa935e848
    internal-label: Shipping/Delivery
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce 2.4.0: Braintree not in Multiple Addresses checkout

This article provides a workaround for an Adobe Commerce 2.4.0 known issue where Braintree payment methods are not included in working with Multiple Addresses checkout. Please note that the issue was fixed in Adobe Commerce 2.4.1.

Note: Adobe Commerce recommends using the [Commerce Marketplace Braintree extension](https://marketplace.magento.com/paypal-module-braintree.html) for versions 2.3 and later in order to keep PSD compliance. The extension does not offer the multi-address checkout functionality.

## Affected products and versions

* Adobe Commerce on-premises v2.4.0
* Adobe Commerce on cloud infrastructure v2.4.0

## Issue

<u>Prerequisites</u>:

The core Braintree integration is used.

<u>Steps to reproduce</u>:

1. Go to the storefront.
1. Log in as a customer.
1. Add a product to the cart.
1. Open your cart.
1. Press **View and Edit Cart**.
1. Press **Check Out with Multiple Addresses**.
1. Press **Go to Shipping Information**.
1. Press **Continue to Billing Information**.

<u>Expected result</u>:

Braintree is available as a payment method.

<u>Actual result</u>:

Braintree is not available as a payment method.

## Workaround

Do not enable multi-address options if using Braintree in Adobe Commerce 2.4.0. This issue was fixed in Adobe Commerce 2.4.1.
