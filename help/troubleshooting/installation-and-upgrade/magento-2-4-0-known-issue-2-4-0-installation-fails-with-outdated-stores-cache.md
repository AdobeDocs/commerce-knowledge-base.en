---
title: Adobe Commerce 2.4.0 installation fails with outdated stores cache
description: 'This article provides a solution for the issue where your Adobe Commerce 2.4.0 installation fails with the error message: *The default website isn''t defined. Set the website and try again.* displayed in the console.'
exl-id: 0680199b-7e47-4a8c-91fe-9f6c32839a0e
feature: B2B, Cache, Console, Install, Upgrade
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 6388cf7b-8a81-5248-a1e4-7bb57bbe250f
    internal-label: Install
  - id: a8ae7a5a-6cdc-5922-bd0d-6feb44b04984
    internal-label: Upgrade
  - id: bd989d82-1e15-4534-88db-f1f51dd77ffa
    internal-label: Accounts
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
  - id: 125c1f49-aefd-5f34-a252-288937f95f6b
    internal-label: Marketing Tools
subfeature_v2:
  - id: f56d26ed-050b-4fb7-b29b-8e6e994e80a2
    internal-label: B2B
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
  - id: c4af0798-d497-5e6b-8380-19812c26d00a
    internal-label: Console
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
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
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2-4-0-braintree-not-in-multiple-addresses-checkout.md)

