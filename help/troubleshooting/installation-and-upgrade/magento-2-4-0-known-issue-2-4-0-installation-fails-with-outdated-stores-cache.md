---
title: Adobe Commerce 2.4.0 installation fails with outdated stores cache
description: "This article provides a solution for the issue where your Adobe Commerce 2.4.0 installation fails with the error message: *The default website isn't defined. Set the website and try again.* displayed in the console."
exl-id: 0680199b-7e47-4a8c-91fe-9f6c32839a0e
feature: B2B, Cache, Console, Install, Upgrade
role: Developer
---
# Adobe Commerce 2.4.0 installation fails with outdated stores cache

This article provides a solution for the issue where your Adobe Commerce 2.4.0 installation fails with the error message: *The default website isn't defined. Set the website and try again.* displayed in the console.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.4.0
* Adobe Commerce on-premises 2.4.0

## Issue

<u>Prerequisites:</u>
A third-party extension with dependencies on APIs for the Store module in CLI commands is configured as required in `composer.json`. This causes the installation of Adobe Commerce 2.4.0 to fail with an error message: *The default website isn't defined. Set the website and try again.* displayed in the console.

## Cause

The issue appears for the third-party extensions which have dependencies on stores in their CLI commands. One is Amazon Sales Channels.

## Solution

Before the installation of Adobe Commerce 2.4.0, merchants have to:

1. Remove these third-party extensions from `composer.json`.
1. Install Adobe Commerce without extensions.
1. Add the extensions after the installation.

The issue will be fixed in the scope of 2.4.1 release.

## Related readings in our support knowledge base:

* [Adobe Commerce 2.4.0 known issue: missing "Refund" label in Klarna](/help/troubleshooting/payments/magento-2-4-0-known-issue-missing-refund-label-in-klarna.md)
* [Adobe Commerce 2.4.0, 2.4.1: Enable Braintree Venmo partial invoice issue](/help/troubleshooting/payments/magento-2-4-0-2-4-1-enable-braintree-venmo-partial-invoice-issue.md)
* [Adobe Commerce 2.4.0 known issue: Error message selecting local payment method displayed for some countries during checkout](/help/troubleshooting/payments/magento-2-4-0-checkout-error-selecting-local-payments.md)
* [Adobe Commerce 2.4.0 known issue: Amazon Pay enabled, payment methods missing when Return to standard checkout used](/help/troubleshooting/payments/magento-2-4-0-known-issue-amazon-pay-no-payment-methods.md)
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2-4-0-b2b-admin-can-t-add-configurable-product-to-quote.md)
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2-4-0-braintree-not-in-multiple-addresses-checkout.md)

