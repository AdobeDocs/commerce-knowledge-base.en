---
title: 'Adobe Commerce 2.4.0, 2.4.1: Enable Braintree Venmo partial invoice'
description: This article describes a known Adobe Commerce 2.4.0 and 2.4.1 issue, where partial invoice is not available for orders placed using Braintree through Venmo.
exl-id: ef6c8aa4-a2a7-4e07-a957-23173017baf2
feature: Invoices, Orders, Payments
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 591c578b-908e-5b79-a9d3-931dfe60c24c
    internal-label: Invoices
  - id: 4820f335-ec9f-5611-8fe3-f5b7e3e56967
    internal-label: Orders
  - id: 3dcbfa9e-51f8-569c-a0e4-7f59098f730f
    internal-label: Payments
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce 2.4.0, 2.4.1: Enable Braintree Venmo partial invoice

This article describes a known Adobe Commerce 2.4.0 and 2.4.1 issue, where partial invoice is not available for orders placed using Braintree through Venmo.

## Affected products and versions

* Adobe Commerce on-premises 2.4.0 and 2.4.1
* Adobe Commerce on cloud infrastructure 2.4.0 and 2.4.1

## Issue

<u>Prerequisites:</u>

In the Braintree payment method configuration, set **Enable Venmo through Braintree** = *Yes* with **Payment Action** = *Authorization*; **Enable Vault for Card Payments** = *No*.

<u>Steps to reproduce:</u>

1. Create an order for two or more products, using Venmo (Braintree) as a payment method.
1. Open the order in the Commerce Admin.
1. Create an invoice for one of the ordered products.
1. Try to create invoice for the rest ordered products.

<u>Expected result:</u>

Invoice created.

<u>Actual result:</u>

The following error message is displayed: *The "vault\_capture" command doesn't exist. Verify the command and try again.*

## Workaround

Capture the whole amount when creating invoices for orders placed using Braintree through Venmo.
