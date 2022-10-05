---
title: "Adobe Commerce 2.4.2: Braintree Venmo payment does not work"
labels: troubleshooting,2.4.2,Braintree Venmo payment,Adobe Commerce,Magento,cloud infrastructure,known issue,orders,on-premises
description: "This article describes a known Adobe Commerce 2.4.2 issue where orders are not generated when using Braintree Venmo during checkout. There is no resolution available at this time."
---

# Adobe Commerce 2.4.2: Braintree Venmo payment does not work

This article describes a known Adobe Commerce 2.4.2 issue where orders are not generated when using Braintree Venmo during checkout. There is no resolution available at this time.

## Affected products and versions

* Adobe Commerce (all deployment methods) 2.4.2

## Issue

 <u>Precondition</u> :

Enable Venmo payment in Braintree configuration.

 <u>Steps to reproduce</u> :

1. On the storefront, add any item to the shopping cart.
1. Proceed to **Checkout**.
1. Select the appropriate shipping method.
1. Select **Venmo** as payment method.
1. Click **Pay with Venmo**.
1. Click **Place order**.

 <u>Actual results</u>:

 The order is not created in Adobe Commerce code after the customer is redirected back to the store from the Venmo app, and no error message appears. The order is created in Braintree.

 <u>Expected results</u>:

 The order is created in Adobe Commerce after the customer is redirected back to the store from the Venmo app, and the order is created in Braintree, as expected.

## Solution

There is no resolution available at this time.