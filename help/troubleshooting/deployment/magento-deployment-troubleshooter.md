---
title: Adobe Commerce deployment troubleshooter
description: Stuck deployments and failed deployments on Adobe Commerce can be solved using the Deployment troubleshooter tool. Click on each question to reveal the answer in each step of the troubleshooter.
exl-id: 5141e079-be61-44c2-8bff-c4b13cb7e07c
feature: "Build, Deploy"
---
# Adobe Commerce deployment troubleshooter

Stuck deployments and failed deployments on Adobe Commerce can be solved using the Deployment troubleshooter tool. Click on each question to reveal the answer in each step of the troubleshooter.

## Step 1 - Verify the service is running {#step-1}

+++**Is Adobe Commerce on cloud infrastructure service up?**

Stuck Deployment – Is Adobe Commerce on cloud infrastructure service up? Check [Adobe Commerce Cloud](https://status.adobe.com/products/3350/).

a. YES – Proceed to [Step 2](#step-2).  
b. NO – Maintenance or global outages. Check for estimated duration and updates.

+++

## Step 2 - Check deployments in other environments {#step-2}

+++**Are there deployments in other environments that are blocking the deployment in the existing environment?**

To get a list of ongoing activities run the following command using magento-cloud CLI (if you have only been added to one cloud project):

```bash
magento-cloud --state=in_progress
```

To get a list of ongoing activities run the following command using magento-cloud CLI (if you have been added to multiple projects):

```bash
magento-cloud -p <project-id or project-url> --state=in_progress
```

To find information about an existing deployment activity (refer to [Checking deployment log if Cloud UI has “log snipped” error](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/checking-deployment-log-if-the-cloud-ui-shows-log-snipped-error.html)
for details) you can run this command to obtain a running log of that activity:

```bash
magento-cloud activity:log <activity-id> [OPTIONAL: <-p project-id or project-url>]
```

a. YES – Troubleshoot the other environment blocking deployment in the existing environment. Proceed to [Step 3](#step-3).

b. NO – Troubleshoot the current environment. Proceed to [Step 3](#step-3).

+++


## Step 3 - Verify SSH on all nodes {#step-3}

+++**SSH successful to all nodes?**

a. YES – Proceed to [Step 4](#step-4).  
b. NO – [Submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

+++

## Step 4 - Verify all services running {#step-4}

+++**All services running?**

a. YES – Proceed to [Step 5](#step-5).  
b. NO – [Submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

+++

## Step 5 - Verify Bitbucket running {#step-5}

+++**Using Bitbucket?**

a. YES – Check [status.bitbucket.com](https://bitbucket.status.atlassian.com/).  
b. NO – Check deployment log errors in the [Build and Deploy logs](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/test/log-locations.html). Proceed to [Step 6](#step-6).

+++

## Step 6 - Check error codes {#step-6}

+++**Error code reported?**

a. YES – Proceed to [Step 7](#step-7).  
b. NO – Proceed to [Step 8](#step-8).

+++

## Step 7 - 403 Forbidden error {#step-7}

+++**403 Forbidden?**

a. YES – Proceed to [Step 16](#step-16).
b. NO – Proceed to [Step 9](#step-9).

+++

## Step 8 - Verify cron jobs running {#step-8}

+++**Are cron jobs currently running?**

a. YES – Log in by ssh on the integration branch (e.g., primary). Kill and unlock cron jobs. This will kill cron jobs and reset the status. Run `php vendor/bin/ece-tools cron:kill` and then `php vendor/bin/ece-tools cron:unlock`. If you were in the process of merging one environment into another, check both environments for running crons.  
b. NO – Proceed to [Step 17](#step-17).

+++

## Step 9 - Application deployable to remote cluster error {#step-9}

+++**Unable to upload application to the remote cluster error?**

a. YES – Proceed to [Step 10](#step-10).  
b. NO – Proceed to [Step 11](#step-11).

+++

## Step 10 - Check sufficient storage {#step-10}

+++**Available storage okay?**

a. YES – Proceed with [Step 11](#step-11).  
b. NO – Review [Manage disk space](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space.html).

+++

## Step 11 - Verify disk space {#step-11}

+++**_file could not be written Warning_?**

a. YES – Please [increase the disk value in .magento.app.yaml](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space.html#application-disk-space) and redeploy. If this does not work, [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).  
b. NO – Proceed with [Step 12](#step-12).

+++

## Step 12 - Environment redeployment failed error {#step-12}

+++**Environment redeployment failed error?**

a. YES – Proceed with [Step 13](#step-13).  
b. NO – Proceed with [Step 8](#step-8).

+++

## Step 13 - Check for Elasticsearch upgrade fail {#step-13}

+++**Elasticsearch being upgraded or deployed?**

a. YES – Elasticsearch failed upgrade steps. Refer to [Elasticsearch software compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html). If the Elasticsearch upgrade still doesn't work, [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket). **Note**: On Adobe Commerce on cloud infrastructure, please be aware that service upgrades cannot be pushed to the production environment without 48 business hours' notice to our infrastructure team. This is required as we need to ensure that we have an infrastructure support engineer available to update your configuration within the desired timeframe with minimal downtime to your production environment. So 48 hours prior to when your changes need to be on production, [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) detailing your required service upgrade and stating the time when you want the upgrade process to start.  
b. NO – Proceed to [Step 14](#step-14).

+++

## Step 14 - Check space limits {#step-14}

+++**File system out of inodes or space?**

a. YES – See [Manage disk space](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space.html#application-disk-space).  
b. NO – Proceed to [Step 15](#step-15).

+++

## Step 15 - Elasticsearch version error {#step-15}

+++**Error about Elasticseach versions?**

a. YES – Proceed to [Step 16](#step-16).  
b. NO – Proceed to [Step 21](#step-21).

+++

## Step 16 - Verify Composer config {#step-16}

+++**Composer config correct?**

a. YES – Proceed to [Step 10](#step-10).  
b. NO – Review [Composer Troubleshooter webpage](https://getcomposer.org/doc/articles/troubleshooting.md).

+++

## Step 17 - Check for long running processes {#step-17}

+++**Long running processes(es)?**

a. YES – Identify long running processes and then kill processes:
1. Run the following command in the terminal: `ps aufx`.
1. Locate the PID of the long-running process.
1. Terminate the process using `kill -9 <PID>`.

Monitor deployments for reoccurrence.  

b. NO – Proceed to [Step 18](#step-18).

+++

## Step 18 - Check for post hook failure {#step-18}

+++**Post hook failure/hang?**

a. YES – Database: [Free disk space](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space.html#allocate-disk-space), corruption, incomplete/corrupted tables.  
b. NO – Proceed to [Step 19](#step-19).

+++

## Step 19 - Check if third-party extensions block deployment {#step-19}

+++**Using third-party extensions?**

a. YES – Try [Disabling the third-party extensions](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure-store/extensions.html) and running the deployment (to see if they are the cause of the problem), especially if there are extension names in any errors.  
b. NO – Proceed to [Step 20](#step-20).

+++

## Step 20 - Check for slow queries {#step-20}

+++**Long running queries?**

[Check slow query log and MySQL show processlist](/help/troubleshooting/database/checking-slow-queries-and-processes-mysql.md).

a. YES – Kill any long running queries. Review [MySQL Kill Syntax.](https://dev.mysql.com/doc/refman/8.0/en/kill.html)  
b. NO – [Submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

+++

## Step 21 - Downgrade Elasticsearch version {#step-21}

+++**Downgrading Elasticsearch versions?**

a. YES – Can't be done through configuration. [Submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).  
b. NO – [Submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

+++

[Back to Step 1](#step-1)
