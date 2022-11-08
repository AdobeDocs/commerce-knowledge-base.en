---
title: 'Adobe Commerce 2.4.0 known issue: Klarna On-Site Messaging blank pages'
description: This article describes a known Adobe Commerce 2.4.0 issue with Klarna payment method, where enabling Klarna on-site messaging without specifying a design theme, results in not displaying product pages on the storefront correctly (product pages appear blank).
exl-id: f0f9edfc-eaad-4947-9200-41e217bfbe84
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
