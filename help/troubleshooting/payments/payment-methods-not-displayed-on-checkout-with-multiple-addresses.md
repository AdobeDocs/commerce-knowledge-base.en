---
title: Payment methods not displayed on checkout with multiple addresses
description: This article explains that most of the payment methods are not displayed on checkout when multiple shipping addresses are specified, because the functionality is only implemented for Cybersource.
exl-id: 68a9ee77-d0ef-43c5-9667-6d099b797666
feature: Checkout, Orders, Payments, Shipping/Delivery
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
  - id: 04d3134c-2afb-5bd7-ac14-e19fa935e848
    internal-label: Shipping/Delivery
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Payment methods not displayed on checkout with multiple addresses

This article explains that most of the payment methods are not displayed on checkout when multiple shipping addresses are specified, because the functionality is only implemented for Cybersource.

## Affected products and versions

* Adobe Commerce on-premises 2.x.x
* Adobe Commerce on cloud infrastructure 2.x.x

>[!NOTE]
>
>The core Adobe Commerce Cybersource payment integration is deprecated since 2.3.3 and will be completely removed in 2.4.0. Use the [official extension](https://marketplace.magento.com/cybersource-global-payment-management.html) from marketplace instead.

## Issue

<u>Prerequisites</u>: In the Commerce Admin, enable and configure PayPal and Cybersource payment methods, and enable Multishipping for your store.

<u>Steps to reproduce</u>:

1. On the storefront, add multiple products to the cart.
1. Go to the shopping cart page.
1. Click **Check Out with Multiple Addresses**.
1. Log in or create account.
1. Split up products between the addresses on the Ship to Multiple Addresses page.
1. Click **Go to Shipping Information**.
1. Select shipping methods for each shipment.
1. Click **Continue to Billing Information**.

<u>Expected result</u>: PayPal and Cybersource are available as payment options.

<u>Actual result</u>: Only Cybersource appears as available payment option.

## Cause

Currently Cybersource is the only supported live payment method for multishipping checkout, starting from version 2.2.4. Support for multishipping will likely be built for each payment method one by one. No exact dates or release numbers can be provided at the moment.
