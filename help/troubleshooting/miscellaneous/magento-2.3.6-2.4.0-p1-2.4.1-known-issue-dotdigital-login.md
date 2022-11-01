---
title: "Adobe Commerce 2.3.6, 2.4.0-p1, 2.4.1 known issue: dotdigital login"
description: "This article describes an Adobe Commerce 2.3.6, 2.4.0-p1, and 2.4.1 known issue where it is impossible to log in to [dotdigital](https://dotdigital.com/) via the Admin Panel when the dotdigital account is enabled."
---

# Adobe Commerce 2.3.6, 2.4.0-p1, 2.4.1 known issue: dotdigital login

This article describes an Adobe Commerce 2.3.6, 2.4.0-p1, and 2.4.1 known issue where it is impossible to log in to [dotdigital](https://dotdigital.com/) via the Admin Panel when the dotdigital account is enabled.

## Affected products and versions

* Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.6 (Safari browser only)
* Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.4.0-p1 (Safari browser only)
* Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.4.1 (Safari browser only)

## Issue

<u>Prerequisites</u>:

1. dotdigital account exists.
1. Valid dotdigital API credentials exist in Adobe Commerce.

<u>Steps to reproduce</u>:

1. Go to **Stores** > **Configuration** > **DOTDIGITAL** > **Chat Settings** > **Enabled** is set to *Yes.*
1. Click on **Configure** in **Configure Chat Widget** or **Configure Chat Teams**.

<u>Expected results</u>:

The chat settings page should open successfully via Admin Panel.

<u>Actual results</u>:

Unable to log in to dotdigital.

## Solution

Workaround: use an alternative browser to Safari for this particular situation.

## Related Reading

 [Adobe Commerce 2.4.1 Known Issue - Vertex address not validating with different shipping/billing addresses](https://support.magento.com/hc/en-us/articles/360050139631) in our support knowledge base. 

