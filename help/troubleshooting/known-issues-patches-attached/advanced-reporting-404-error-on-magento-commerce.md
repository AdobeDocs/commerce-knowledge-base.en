---
title: [!DNL Advanced Reporting] 404 error on Adobe Commerce
description: This article provides a patch for the Adobe Commerce issue when a merchant gets a 404 error when they attempt to access [[!DNL Advanced Reporting]](https://experienceleague.adobe.com/docs/commerce-admin/config/general/advanced-reporting.html). After this patch is installed, users will be able to access [!DNL Advanced Reporting].
exl-id: bac61704-44fe-4bd2-b342-af90219231ef
---
# [!DNL Advanced Reporting] 404 error on Adobe Commerce

This article provides a patch for the Adobe Commerce issue when a merchant gets a 404 error when they attempt to access [[!DNL Advanced Reporting]](https://experienceleague.adobe.com/docs/commerce-admin/config/general/advanced-reporting.html). After this patch is installed, users will be able to access [!DNL Advanced Reporting].

To check if this patch could solve this issue, first review the logs by using the following command:

 `zgrep analytics_collect_data var/log/support_report.log var/log/support_report.log.1.gz`

If you see the `Not valid cipher` error, apply the attached patch.

## Affected products and versions

Adobe Commerce 2.2.6

## Issue

A merchant gets a 404 error when they attempt to access [!DNL Advanced Reporting].

## Solution

To fix the issue, please apply the patch attached to this article. To download it, scroll down to the end of the article and click the file name, or click the following link: [Download MDVA-18980\_EE\_2.2.6\_COMPOSER\_v1](assets/MDVA-18980_EE_2.2.6_COMPOSER_v1.patch.zip)

## How to apply the patch

See [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) for instructions.

## Attached files
