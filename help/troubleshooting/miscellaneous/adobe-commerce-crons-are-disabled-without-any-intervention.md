---
title: Adobe Commerce [!DNL crons] disabled without intervention
description: Use this article to fix the issue where [!DNL crons] are disabled without intervention.
exl-id: 5172d2ae-53ad-4db6-ae00-7b27c96911e9
---
# Adobe Commerce crons disabled without intervention

This article provides a solution for when [!DNL crons] are disabled without intervention. 

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all [supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf). 

## Issue

Your [!DNL crons] are disabled after deployment. 

<u>Steps to reproduce</u>:

Deploy.

<u>Expected result</u>:

Your [!DNL crons] are running.

<u>Actual result</u>:

Your [!DNL crons] are disabled after deployment. 

## Cause

An issue with the [!DNL OPcache] settings.

## Solution

Upgrade [!DNL ECE Tools] to the latest version [2002.1.13](https://devdocs.magento.com/cloud/release-notes/ece-release-notes.html#v2002113).

## Related reading

* [Slow performance, slow and long running [!DNL crons]](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/slow-performance-slow-and-long-running-crons.html) in our support knowledge base. 
* [[!DNL Cron] tasks lock tasks from other groups](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cron-tasks-lock-tasks-from-other-groups.html?lang=en) in our support knowledge base. 
* [[!DNL Cron] job is stuck in "running" status](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cron-job-is-stuck-in-running-status.html?lang=en) in our support knowledge base.
