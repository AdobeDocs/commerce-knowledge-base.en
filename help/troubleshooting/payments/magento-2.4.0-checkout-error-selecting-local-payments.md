---
title: 'Adobe Commerce 2.4.0: Checkout error selecting local payments'
description: 'This article talks about a solution for a known issue in Adobe Commerce during checkout where an error message appears when selecting a local payment method for some countries. This occurs for the countries: Belgium, Italy, Netherlands, Poland, and Spain.'
exl-id: de2eafb0-d03c-4ff8-9615-0f2676d95848
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
* Configure [Braintree Payment Method](https://devdocs.magento.com/guides/v2.4/graphql/payment-methods/braintree.html).

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

* [Adobe Commerce 2.4.0 known issue: raw message data display on storefront](https://support.magento.com/hc/en-us/articles/360045804332)
* [Adobe Commerce 2.4.0 known issue: Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2.4.0-braintree-not-in-multiple-addresses-checkout.md)
* [Adobe Commerce 2.4.0 known issue: returns edit page stops working when creating shipping label](/help/troubleshooting/known-issues-patches-attached/magento-2.4.0-patch-returns-shipping-label-creation-issue.md)
* [Adobe Commerce 2.4.0 known issue: refresh on Customer's Activities does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-refresh-on-customer-activities-does-not-work.md)
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2.4.0-b2b-admin-can-t-add-configurable-product-to-quote.md)
