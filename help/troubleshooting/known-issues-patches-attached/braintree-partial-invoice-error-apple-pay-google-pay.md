---
title: 'Adobe Commerce 2.4.4: Unable to create partial invoices'
description: This article provides a hotfix for the issue where users are not able to create partial invoices when using Apple Pay or Google Pay through Braintree as payment methods.
exl-id: bf78cc07-9dc7-4eb8-bfdf-57ea5131effb
feature: Invoices, Orders, Payments
role: Developer
---
# Adobe Commerce 2.4.4: Unable to create partial invoices

This article provides a hotfix for the issue where users are not able to create partial invoices when using Apple Pay or Google Pay through Braintree as payment methods.

## Affected products and versions

Adobe Commerce (all deployment methods) 2.4.4

## Issue

When using Apple Pay or Google Pay as payment methods, users get the error “*The ‘vault_capture’ command doesn't exist. Verify the command and try again.*”  while creating partial invoices.

<u>Steps to reproduce</u>:

1. Open your Adobe Commerce website.
1. Add a simple product to the cart (qty 2).
1. Choose **Apple Pay** or **Google Pay** as the payment method from the shopping cart.
1. Place the order.
1. Open order details from the back-end.
1. Create a partial invoice.
1. Create another invoice for the remaining amount.

<u>Expected results</u>:

Partial invoices are created.

<u>Actual results</u>:

The first partial invoice is created. While creating the second partial invoice, users get the following error: *The ‘vault_capture’ command doesn't exist. Verify the command and try again*.

## Cause

Adobe Commerce saves credit card details in the vault to create partial invoices. Currently, there is no functionality to vault Apple Pay and Google Pay.

## Solution

To resolve the issue, apply the following patch:

[Braintree_disabled_partial_capture_for_applepay_googlepay.zip](assets/braintree-disabled-partial-capture-for-applepay-googlepay.zip)

## How to Apply the Patch

See [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) for instructions.
