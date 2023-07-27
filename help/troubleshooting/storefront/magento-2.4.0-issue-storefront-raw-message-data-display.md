---
title: 'Adobe Commerce 2.4.0 issue: storefront raw message data display'
description: This article provides a solution for the issue when all error messages on the storefront display with a "+" sign instead of a space. This solution helps error messages remain readable.
exl-id: f44fe434-a320-4e7e-a876-9575921749f3
feature: Storefront
role: Admin
---
# Adobe Commerce 2.4.0 issue: storefront raw message data display

This article provides a solution for the issue when all error messages on the storefront display with a "+" sign instead of a space. This solution helps error messages remain readable.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.4.0
* Adobe Commerce on-premises 2.4.0.

## Issue

<u>Steps to reproduce:</u>

1. Go to **Create New Account** page on the storefront.
1. Create a new account using a registered email. The following message is displayed:

 `There+is+already+an+account+with+this+email+address.+If+you+are+sure+that+it+is+your+email+address,+click+here+to+get+your+password+and+access+your+account.`

## Cause

The issue is caused by a PHP 7.4.2 issue related to set\\read cookies. See [PHP BUG \#79174 setcookie() encodes space as \`+\`, but $\_COOKIE no longer decodes them](https://bugs.php.net/bug.php?id=79174).

## Solution

To solve this issue, use another version of PHP 7.4.x. PHP 7.4.2 is not supported by Adobe Commerce 2.4.0.

## Related readings in our support knowledge base:

* [Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2.4.0-braintree-not-in-multiple-addresses-checkout.md)
* [Shipping labels creation known issue in Adobe Commerce 2.4.0](/help/troubleshooting/known-issues-patches-attached/shipping-labels-creation-known-issue-in-magento-2.4.0.md)
* [Adobe Commerce 2.4.0 known issue: Refresh on Customer's Activities does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-refresh-on-customer-activities-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: “Add selections to my cart” button does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-add-selections-to-my-cart-does-not-work.md)
