---
title: Customers get logged out or lose cart content on Adobe Commerce storefront
description: This article provides a solution and workaround for the issue, where customers get logged out or lose items from the shopping cart on the storefront, after being re-directed back to the Adobe Commerce store from payment or other third-party services (session cookie "gets lost").
exl-id: 9175570c-b06c-4a65-b8ca-7a12ff266afb
feature: Orders, Page Content, Shopping Cart, Storefront
role: Admin
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 4820f335-ec9f-5611-8fe3-f5b7e3e56967
    internal-label: Orders
  - id: 17d326fa-534a-55a5-b46f-8ae1de1e2f75
    internal-label: Page Content
  - id: df8eaa0e-dd74-553a-8ad5-28129f8e8d3d
    internal-label: Shopping Cart
  - id: d1e21356-0064-4f48-9089-16e3f0dbd2a6
    internal-label: Storefront
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# Customers get logged out or lose cart content on Adobe Commerce storefront

This article provides a solution for the issue, where customers get logged out or lose items from the shopping cart on the storefront, after being re-directed back to the Adobe Commerce store from payment or other third-party services (session cookie "gets lost").

## Affected products and versions

* Adobe Commerce on-premises, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)
* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Issue

 <u>Steps to reproduce:</u>

1. The customer adds products to cart on storefront and proceeds to checkout.
1. The customer is redirected to the third-party site for payment/shipping or other information/service.
1. The customer is redirected back to the store.

 <u>Actual result:</u>

Customer redirected to the empty shopping cart or a blank page.

 <u>Expected result:</u>

Customer redirected to a success payment page (or other success page), without losing the checkout data and progress.

## Cause

The SameSite cookie attribute is set to *Lax* or not specified (which is treated as set to *Lax* ). Having `SameSite` = *Lax* disables transferring a cookie to external URLs via `POST` requests.

## Solution

To solve the issue, contact the third-party service provider and request their developers update their integrations to configure cookie parameters.

## Related reading

 [Chrome SameSite update](https://www.chromestatus.com/feature/5088147346030592)
