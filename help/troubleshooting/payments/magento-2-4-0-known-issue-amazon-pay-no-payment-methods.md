---
title: 'Adobe Commerce 2.4.0 known issue: Amazon pay, no payment methods'
description: This article provides a solution for an Adobe Commerce 2.4.0 known issue where payment methods are missing when customers use **Return to standard checkout**, after they enabled Amazon pay.
exl-id: efd792c7-8970-4366-b9d1-4bf284ea96db
feature: B2B, Orders, Payments
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 4820f335-ec9f-5611-8fe3-f5b7e3e56967
    internal-label: Orders
  - id: 3dcbfa9e-51f8-569c-a0e4-7f59098f730f
    internal-label: Payments
  - id: bd989d82-1e15-4534-88db-f1f51dd77ffa
    internal-label: Accounts
subfeature_v2:
  - id: f56d26ed-050b-4fb7-b29b-8e6e994e80a2
    internal-label: B2B
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce 2.4.0 known issue: Amazon pay, no payment methods

This article provides a solution for an Adobe Commerce 2.4.0 known issue where payment methods are missing when customers use **Return to standard checkout**, after they enabled Amazon pay.

## Affected products and versions

Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure v2.3.5.p1 and v2.4.0

 <u>Steps to reproduce:</u>

1. Navigate to the storefront.
1. Add any item to the cart and proceed to the checkout.
1. Log in to your Amazon Pay account.
1. Select an address and proceed to the checkout.
1. Click **Return to standard checkout**.
1. Proceed to the checkout.

 <u>Expected results:</u>

Payment methods should be displayed after restarting checkout.

 <u>Actual results:</u>

Payment methods are missing.

## Solution

A resolution is planned for 2.4.1.

## Related readings in our support knowledge base:

* [Adobe Commerce 2.4.0 known issue: Error message selecting local payment method displayed for some countries during checkout](/help/troubleshooting/payments/magento-2-4-0-checkout-error-selecting-local-payments.md)
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2-4-0-braintree-not-in-multiple-addresses-checkout.md)
