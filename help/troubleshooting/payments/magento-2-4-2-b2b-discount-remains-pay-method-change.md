---
title: 'Adobe Commerce 2.4.2 B2B: discount remains pay method change'
description: This article describes a known Adobe Commerce 2.4.2 B2B issue where a payment method-tied discount persists after a payment method change at checkout. There is no resolution available at this time.
exl-id: cd863852-403b-404f-8717-c78c238f5f33
feature: B2B, Orders, Payments, Personalization
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 4820f335-ec9f-5611-8fe3-f5b7e3e56967
    internal-label: Orders
  - id: 3dcbfa9e-51f8-569c-a0e4-7f59098f730f
    internal-label: Payments
  - id: f37757d8-3174-5335-b977-1161792f965d
    internal-label: Personalization
  - id: bd989d82-1e15-4534-88db-f1f51dd77ffa
    internal-label: Accounts
subfeature_v2:
  - id: f56d26ed-050b-4fb7-b29b-8e6e994e80a2
    internal-label: B2B
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce 2.4.2 B2B: discount remains pay method change

This article describes a known Adobe Commerce 2.4.2 B2B issue where a payment method-tied discount persists after a payment method change at checkout. There is no resolution available at this time.

## Affected products and versions

* Adobe Commerce 2.4.2
* Adobe Commerce on cloud infrastructure 2.4.2
* B2B for Adobe Commerce 1.3.1


## Issue

 <u>Steps to reproduce</u> :

1. Create a cart **Price Rule** that is tied to a payment method (Example: Paypal users get a 20% discount.).
1. Create a Purchase Order (PO) and select Paypal as the payment method. The discount is applied.
1. The PO is approved.
1. Go to the payment page to complete the order.
1. Select a different payment method.

 <u>Actual results</u> :

The payment method discount remains applied to the order total.  No error message is displayed.The store owner will be able to see this occurred by checking order history.

 <u>Expected results</u> :The payment method discount is removed from the order total, as expected.

## Solution

There is no resolution available at this time.
