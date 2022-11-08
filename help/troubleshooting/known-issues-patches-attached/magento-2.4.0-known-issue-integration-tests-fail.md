---
title: 'Adobe Commerce 2.4.0 known issue: integration tests fail'
description: This article provides a patch for the Adobe Commerce 2.4.0 issue where integration tests are failing because the declaration of `Dotdigitalgroup\Email\Test\Integration\Model\Sync\Importer\ImporterFailedTest::setUp()` is not compatible with PHPUnit 9 which is used for 2.4.0.
exl-id: 8e0ca2da-81d9-4561-a009-593240f46e41
---
# Adobe Commerce 2.4.0 known issue: integration tests fail

This article provides a patch for the Adobe Commerce 2.4.0 issue where integration tests are failing because the declaration of `Dotdigitalgroup\Email\Test\Integration\Model\Sync\Importer\ImporterFailedTest::setUp()` is not compatible with PHPUnit 9 which is used for 2.4.0.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.4.0
* Adobe Commerce on-premises 2.4.0

## Issue

 <u>Steps to reproduce</u>

Run 2.4.0 integration tests.

 <u>Expected result</u>

Tests pass.

 <u>Actual result</u>

 *PHP Fatal error: Declaration of Dotdigitalgroup\\Email\\Test\\Integration\\Model\\Sync\\Importer\\ImporterFailedTest::setUp() must be compatible with PHPUnit\\Framework\\TestCase::setUp(): void in /var/www/vendor/dotmailer/dotmailer-magento2-extension/Test/Integration/Model/Sync/Importer/ImporterFailedTest.php on line 36*

## Solution

Apply the patch provided in this article.

## Patch

The patch is attached to this article. To download it, scroll down to the end of the article and click the file name, or click the following link:

 [BUNDLE-2684-composer.patch](assets/BUNDLE-2684-composer.patch.zip)

### Compatible Adobe Commerce versions:

The patch was created for:

* Adobe Commerce on cloud infrastructure 2.4.0
* Adobe Commerce on-premises 2.4.0

## How to apply the patch

See [How to apply a composer patch provided by Adobe](https://support.magento.com/hc/en-us/articles/360028367731) in our support knowledge base for instructions.

## Attached Files
