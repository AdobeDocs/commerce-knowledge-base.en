---
title: Adobe Commerce crons disabled without intervention
description: Use this article to fix the issue where crons are disabled without intervention. 
---

# Adobe Commerce crons disabled without intervention

This article provides a solution for when DNL crons are disabled without intervention. 

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all [supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf). 

## Issue

Your crons are disabled after deployment. 

<u>Steps to reproduce</u>:

Successfully deploy.

<u>Expected result</u>:

Your crons are running.

<u>Actual result</u>:

Your crons are disabled after deployment. You see _[!UICONTROL INFO: Enable cron]_ in the deploy log.

## Cause

You might not have pulled updates from templates. Check OPcache configuration as the [!UICONTROL op-exclude.txt] file could contain incorrect paths. For steps, refer to _Find OPcache configuration settings_ in [Installation Guide > PHP settings](https://experienceleague.adobe.com/docs/commerce-operations/installation-guide/prerequisites/php-settings.html).

## Solution

Upgrade [!DNL ECE Tools] to the latest version [2002.1.13](https://devdocs.magento.com/cloud/release-notes/ece-release-notes.html#v2002113).

## Related reading

* [Slow performance, slow and long running crons](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/slow-performance-slow-and-long-running-crons.html) in our support knowledge base. 
* [[!DNL Cron] tasks lock tasks from other groups](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cron-tasks-lock-tasks-from-other-groups.html?lang=en) in our support knowledge base. 
* [[!DNL Cron] job is stuck in "running" status](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cron-job-is-stuck-in-running-status.html?lang=en) in our support knowledge base.
