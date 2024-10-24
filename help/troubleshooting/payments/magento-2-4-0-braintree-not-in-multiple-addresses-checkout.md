---
title: 'Adobe Commerce 2.4.0: Braintree not in Multiple Addresses checkout'
description: This article provides a workaround for an Adobe Commerce 2.4.0 known issue where Braintree payment methods are not included in working with Multiple Addresses checkout. Please note that the issue was fixed in Adobe Commerce 2.4.1.
exl-id: efde0bba-fd4a-490b-becb-856cb9ea58a5
feature: Checkout, Compliance, Orders, Payments, Shipping/Delivery
role: Developer
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

## Related reading in our support knowledge base

* [Adobe Commerce 2.4.0 known issue - refresh on Customer's Activities does not work](/help/troubleshooting/miscellaneous/magento-2-4-0-refresh-on-customer-activities-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: raw message data display on storefront](/help/troubleshooting/storefront/magento-2-4-0-issue-storefront-raw-message-data-display.md)
* [Adobe Commerce 2.4.0 known issue - Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2-4-0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: “Add selections to my cart” button does not work](/help/troubleshooting/miscellaneous/magento-2-4-0-add-selections-to-my-cart-does-not-work.md)
