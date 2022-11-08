---
title: Google Analytics is not tracking conversion data
description: This article provides a patch for the known Adobe Commerce 2.2.4 issue related to Google Analytics not tracking the conversion data.
exl-id: b9012fd1-4f90-41e9-9559-0343ee052ec6
---
# Google Analytics is not tracking conversion data

This article provides a patch for the known Adobe Commerce 2.2.4 issue related to Google Analytics not tracking the conversion data.

>[!NOTE]
>
>The issue was fixed in Adobe Commerce 2.2.6.

## Issue

The conversion data was not tracked by Google Analytics due to an error in the Google Analytics component code.

 <u>Steps to reproduce</u>:

1. Enable and configure the Google Analytics functionality in the Commerce Admin under **Stores** > **Settings** > **Configuration** > **Sales** > **Google API** > **Google Analytics**.
1. Click **Save Config**.
1. Place an order on the storefront.
1. Go to **Google Analytics Dashboard** > **Conversions** > **Overview**.
1. Set the date range to the current date.

 <u>Expected result</u>:

The order appears in the conversion data.

 <u>Actual result</u>:

The order does not appear in the conversion data.

## Solution

The patch fixes the error in the Google Analytics component code. After applying the patch conversion data will be tracked by Google Analytics.

## Patch

The patch is attached to this article. To download it, scroll down to the end of the article and click the file name or click the following link:

 [Download MDVA-11263\_EE\_2.2.4\_v1.composer.patch](assets/MDVA-11263_EE_2.2.4_v1.composer.patch.zip)

### Compatible Adobe Commerce versions:

The patch was created for:

* Adobe Commerce on-premises 2.2.4

The patch is also compatible (but might not solve the issue) with the following Adobe Commerce versions and editions:

* Adobe Commerce on-premises 2.2.5
* Adobe Commerce on cloud infrastructure 2.2.4, 2.2.5

## How to apply the patch

See [How to apply a composer patch provided by Adobe Commerce](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) for instructions.

## Attached Files
