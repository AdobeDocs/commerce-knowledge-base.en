---
title: 'Adobe Commerce 2.4.0 known issue: Amazon pay, no payment methods'
description: This article provides a solution for an Adobe Commerce 2.4.0 known issue where payment methods are missing when customers use **Return to standard checkout**, after they enabled Amazon pay.
exl-id: efd792c7-8970-4366-b9d1-4bf284ea96db
feature: B2B, Orders, Payments
role: Developer
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
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2-4-0-b2b-admin-can-t-add-configurable-product-to-quote.md)
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2-4-0-braintree-not-in-multiple-addresses-checkout.md)
