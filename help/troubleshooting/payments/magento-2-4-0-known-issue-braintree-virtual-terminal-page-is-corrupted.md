---
title: Adobe Commerce 2.4.0 Braintree Virtual Terminal page corrupted
description: This article provides a patch for the known Adobe Commerce 2.4.0 issue, where the Braintree Virtual Terminal page does not load the proper UI elements or a proper error message if Braintree is not configured.
exl-id: 1d4d762d-2ab3-4752-ad6d-1eb6a179917d
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
# Adobe Commerce 2.4.0 Braintree Virtual Terminal page corrupted

This article provides a patch for the known Adobe Commerce 2.4.0 issue, where the Braintree Virtual Terminal page does not load the proper UI elements or a proper error message if Braintree is not configured.

## Affected products and versions

* Adobe Commerce on-premises 2.4.0
* Adobe Commerce on cloud infrastructure 2.4.0

## Issue

### Scenario 1: Braintree payment method is configured

 <u>Steps to reproduce:</u>

In Commerce Admin, go to **Sales** > **Braintree Virtual Terminal** . ** **

 <u>Expected result:</u>

The **Braintree Virtual Terminal** page loads with proper UI.

 <u>Actual result:</u>

The UI of the **Braintree Virtual Terminal** page is broken.

### Scenario 2: Braintree payment method is configured

 <u>Steps to reproduce:</u>

In Commerce Admin, go to **Sales** > **Braintree Virtual Terminal** . ** **

 <u>Expected result:</u>

The **Braintree Virtual Terminal** page loads with proper UI and a warning is displayed informing that Braintree is not yet configured.

 <u>Actual result:</u>

The UI of the **Braintree Virtual Terminal** page is broken and no warning is displayed.

## Solution

Apply the patch provided in this article.

## Patch

The patch is attached to this article. To download it, scroll down to the end of the article and click the file name, or click the following link:

 [BUNDLE-2670-composer.patch](assets/BUNDLE-2670-composer.patch.zip)

### Compatible Adobe Commerce versions:

The patch was created for:

* Adobe Commerce on cloud infrastructure 2.4.0
* Adobe Commerce on-premises 2.4.0

## How to apply the patch

See [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/en/docs/support-resources/adobe-support-tools-guide/adobe-commerce-support/how-to-apply-a-composer-patch-provided-by-magento) for instructions.

## Attached Files
