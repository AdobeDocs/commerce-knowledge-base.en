---
title: Reset stuck Adobe Commerce on cloud infrastructure cron jobs manually
description: Adobe Commerce on cloud infrastructure cron jobs don't finish executing, get stuck, and prevent other cron jobs from running. This article shows how to reset the stuck cron jobs manually.
exl-id: aec6de8e-c3a9-4a6d-8ecd-a213e77c97a1
---
# Reset stuck Adobe Commerce on cloud infrastructure cron jobs manually

Adobe Commerce on cloud infrastructure cron jobs don't finish executing, get stuck, and prevent other cron jobs from running. This article shows how to reset the stuck cron jobs manually.

Use this command with caution! We recommend reading the [Reset cron jobs](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cron-job-is-stuck-in-running-status.html) article in our support knowledge base for more details.

## Steps

1. Make sure the Adobe Commerce [ECE-Tools](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/dev-tools/ece-tools/update-package.html) are [patched](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) to [v2002.0.4](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/dev-tools/ece-tools/update-package.html).
1. [SSH to your environment](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/cli-branches.html).
1. Execute this command: `./vendor/bin/ece-tools cron:unlock`

## Warnings

* The command resets **all** cron jobs, including those currently running; **use it in exceptional cases only**.
* Avoid using this solution when indexers are running.

## Read it in our support knowledge base:

 [Reset cron jobs](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cron-job-is-stuck-in-running-status.html)
