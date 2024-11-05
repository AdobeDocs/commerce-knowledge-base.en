---
title: '[!DNL Cron] tasks lock tasks from other groups'
description: This article provides a solution for the Adobe Commerce on cloud infrastructure issue related to certain long-run [!DNL cron] jobs blocking other [!DNL cron] jobs.
exl-id: b5b9e8b3-373c-4f93-af9c-85da84dbc928
feature: Configuration
role: Developer
---
# [!DNL Cron] tasks lock tasks from other groups

This article provides a solution for the Adobe Commerce on cloud infrastructure issue related to certain long-run [!DNL cron] jobs blocking other [!DNL cron] jobs.

## Affected products and versions

* Adobe Commerce on cloud infrastructure Pro plan architecture
* Onboard earlier than May 2019

## Issue

On Adobe Commerce for cloud, when you have complex [!DNL cron] tasks (long-run tasks), they might lock other tasks for execution. For example, the indexers' task reindexes invalidated indexers. It can take a few hours to finish, and it will lock other default [!DNL cron] jobs like sending emails, generating sitemaps, customer notifications, and other custom tasks.

<u>Symptoms</u>:

The processes executed by [!DNL cron] jobs are not performed. For example, product updates are not applied for hours, or customers report not receiving emails.

When you open the `cron_schedule` database table, you see the jobs with `missed` status.

## Cause

Previously, in our cloud environment, the Jenkins server was used to run [!DNL cron] jobs. Jenkins will only run one instance of a job at a time; consequently, there will only be one `bin/magento cron:run` process running at a time.

## Solution

1. Contact [Adobe Commerce support](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) to have self-managed [!DNL crons] enabled.
1. Edit the `.magento.app.yaml` file in the root directory of the code for Adobe Commerce in the [!DNL Git] branch. Add the following:

   ```yaml
     crons:
     cronrun:
     spec: "* * * * *"
     cmd: "php bin/magento cron:run"
   ```

1. Save the file and push updates to the Staging and Production environments (the same way you do it for Integration environments).

>[!NOTE]
>
>There's no need to transfer old [!DNL cron] configurations where multiple `cron:run` are present to the new [!DNL cron] schedule; the regular `cron:run` task, added as described above, is enough. Though, it is required to transfer your custom jobs if you had any.

### Check if you have self-managed [!DNL cron] enabled (only for Cloud Pro Staging and Production)

To check if the self-managed [!DNL cron] is enabled, run the `crontab -l` command and observe the result:

* Self-managed [!DNL cron] is enabled, if you are able to see the tasks, like the following:

    ```bash
    username@hostname:~$ crontab -l    # Crontab is managed by the system, attempts to edit it directly will fail.
    SHELL=/etc/platform/username/cron-run    MAILTO=""    # m h dom mon dow job_name    * * * * * cronrun
    ```

* The self-managed [!DNL cron] is not enabled if you are not able to see the tasks and get the *"you are not allowed to use this program"* error message.

>[!NOTE]
>
>The command mentioned above to check if self-managed [!DNL cron] is enabled does not apply on a Starter plan and in the development/integration environment.

## Related reading

* [Set up [!DNL cron] jobs](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cli/configure-cron-jobs) in our developer documentation
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
