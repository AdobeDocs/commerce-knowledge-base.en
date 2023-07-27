---
title: 'Adobe Commerce 2.3.6: endless spinner displayed on address save'
description: This article describes a known Adobe Commerce 2.3.6 issue, where the waiting spinner is displayed indefinitely when saving an address in My account on the storefront.
exl-id: 63841114-167e-4915-b6ed-ee0ef4eae36e
feature: Shipping/Delivery, Orders, Checkout
role: Developer
---
# Adobe Commerce 2.3.6: endless spinner displayed on address save

This article describes a known Adobe Commerce 2.3.6 issue, where the waiting spinner is displayed indefinitely when saving an address in My account on the storefront.

## Affected products and versions

* Adobe Commerce 2.3.6 with Vertex integration enabled (Firefox browser only)

## Issue

When saving an address in My account section on the storefront, sometimes the waiting spinner is displayed indefinitely due to an error in Vertex core JS.

## Workaround

Workaround: use an alternative browser to Firefox.

The issue was fixed in Adobe Commerce 2.3.1.

## Related reading

* [Different addresses not allowed when unselecting 'My billing and shipping address are the same' using VertexAddress Cleansing](/help/troubleshooting/miscellaneous/vertex-address-cleansing-different-addresses-not-allowed.md) in our support knowledge base.
* [Adobe Commerce 2.4.1 Vertex Address validation message post address update](/help/troubleshooting/miscellaneous/magento-2.4.1-vertex-address-validation-message-post-address-update.md) in our support knowledge base.
