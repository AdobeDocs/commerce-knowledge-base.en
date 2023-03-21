---
title: Reset stuck Adobe Commerce on cloud infrastructure cron jobs manually
description: Adobe Commerce on cloud infrastructure cron jobs don't finish executing, get stuck, and prevent other cron jobs from running. This article shows how to reset the stuck cron jobs manually.
exl-id: aec6de8e-c3a9-4a6d-8ecd-a213e77c97a1
---
# Reset stuck Adobe Commerce on cloud infrastructure cron jobs manually

Adobe Commerce on cloud infrastructure cron jobs don't finish executing, get stuck, and prevent other cron jobs from running. This article shows how to reset the stuck cron jobs manually.

Use this command with caution! We recommend reading the [Reset cron jobs](c) article in our support knowledge base for more details.

## Steps

>[!INFO]
>
>From [ECE-Tools v2002.0.4](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/release-notes/cloud-release-archive.html?lang=en#v2002.0.4) you can manually reset stuck cron jobs using a CLI command in all environments via SSH access you can manually reset stuck cron jobs using a CLI comand via SSH access.

1. [SSH to your environment](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/secure-connections.html).
1. Execute this command: `./vendor/bin/ece-tools cron:unlock`

## Warnings

* The command resets **all** cron jobs, including those currently running; **use it in exceptional cases only**.
* Avoid using this solution when indexers are running.

## Read it in our support knowledge base:

 [Reset cron jobs](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cron-job-is-stuck-in-running-status.html)
