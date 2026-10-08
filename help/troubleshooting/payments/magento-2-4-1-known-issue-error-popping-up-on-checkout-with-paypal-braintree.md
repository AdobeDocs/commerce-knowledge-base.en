---
title: 'Adobe Commerce 2.4.1 known issue: error popping up on Checkout with PayPal Braintree'
description: This article describes a known Adobe Commerce 2.4.1 issue, where an error message pops-up and disappears on the Billing step of Checkout if PayPal Braintree payment is used and multiple addresses shipment selected.
exl-id: db3830b2-4885-4d89-85cd-bdcbd4b396e6
feature: Checkout, Orders, Payments
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
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce 2.4.1 known issue: error popping up on Checkout with PayPal Braintree

This article describes a known Adobe Commerce 2.4.1 issue, where an error message pops-up and disappears on the Billing step of Checkout if PayPal Braintree payment is used and multiple addresses shipment selected.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.4.1
* Adobe Commerce on-premises 2.4.1

## Issue

An error message pops-up and disappears on the Billing step of Checkout if PayPal Braintree payment is used and multiple addresses shipment selected.

<u>Steps to reproduce:</u>

1. On the storefront, log in as a customer (optionally could be a guest checkout, if it is enabled in Admin).
1. Add a product to the cart.
1. Click to open the cart preview.
1. Click **View and Edit Cart**.
1. On the Cart page, click **Check Out with Multiple Addresses**.
1. Click **Go to Shipping Information** and specify the addresses.
1. Click **Continue to Billing Information**.
1. Select **PayPal Braintree** and click the **PayPal** button.
1. In the pop-up window, click **Agree & Pay**.

<u>Expected result:</u>

The order is placed without any error.

<u>Actual result:</u>

The order is placed, but with an error. The *PayPal Checkout could not be initialized. Please contact store owner*.  error is displayed for a second and disappears.

## Fix

Since the order placing is not blocked, there is no need to perform workaround steps.
