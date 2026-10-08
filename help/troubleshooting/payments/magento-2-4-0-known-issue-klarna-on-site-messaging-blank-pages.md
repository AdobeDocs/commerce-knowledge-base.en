---
title: 'Adobe Commerce 2.4.0 known issue: Klarna On-Site Messaging blank pages'
description: This article describes a known Adobe Commerce 2.4.0 issue with Klarna payment method, where enabling Klarna on-site messaging without specifying a design theme, results in not displaying product pages on the storefront correctly (product pages appear blank).
exl-id: f0f9edfc-eaad-4947-9200-41e217bfbe84
feature: Orders, Payments
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 4820f335-ec9f-5611-8fe3-f5b7e3e56967
    internal-label: Orders
  - id: 3dcbfa9e-51f8-569c-a0e4-7f59098f730f
    internal-label: Payments
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce 2.4.0 known issue: Klarna On-Site Messaging blank pages

This article describes a known Adobe Commerce 2.4.0 issue with Klarna payment method, where enabling Klarna on-site messaging without specifying a design theme, results in not displaying product pages on the storefront correctly (product pages appear blank).

## Affected products and versions

* Adobe Commerce on-premises 2.4.0
* Adobe Commerce on cloud infrastructure 2.4.0

<u>Prerequisites:</u> Klarna payment method is enabled.

<u>Steps to reproduce:</u>

1. In the Commerce Admin, go to **Stores** > **Configuration** > **Sales** > **Payment Methods** > **Klarna** > **Klarna On-Site Messaging**.
1. Set **Enable** to *Yes*.
1. Leave the **Design theme** field blank.
1. Save configuration by clicking **Save Config**.
1. Go to storefront and navigate to any product page.

<u>Expected result:</u>

The page loads successfully with default design theme applied for Klarna on-site messaging.

<u>Actual result:</u>

A blank page is displayed.

## Solution

If enabling the Klarna on-site messaging, always ensure that the **Design theme** field is not blank.
