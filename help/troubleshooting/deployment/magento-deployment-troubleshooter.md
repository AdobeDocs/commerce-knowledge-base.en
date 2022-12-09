---
title: Adobe Commerce deployment troubleshooter
description: Stuck deployments and failed deployments on Adobe Commerce can be solved using the Deployment troubleshooter tool. Click on each question to reveal the answer in each step of the troubleshooter.
exl-id: 5141e079-be61-44c2-8bff-c4b13cb7e07c
---
# Adobe Commerce deployment troubleshooter

Stuck deployments and failed deployments on Adobe Commerce can be solved using the Deployment troubleshooter tool. Click on each question to reveal the answer in each step of the troubleshooter.

## Step 1

+++**Is Adobe Commerce on cloud infrastructure service up?**

Stuck Deployment – Is Adobe Commerce on cloud infrastructure service up? Check [Adobe Magento Magento Commerce Cloud](https://status.adobe.com/products/3350/).

a. YES – Proceed to [Step 2](#step-2).  
b. NO – Maintenance or global outages. Check for estimated duration and updates.

+++

## Step 2

+++**SSH successful to all nodes?**

a. YES – Proceed to [Step 3](#step-3).  
b. NO – [Submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251).

+++

## Step 3

+++**All services running?**

a. YES – Proceed to [Step 4](#step-4).  
b. NO – [Submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251).

+++

## Step 4

+++**Using Bitbucket?**

a. YES – Check [status.bitbucket.com](https://bitbucket.status.atlassian.com/).  
b. NO – Check deployment log errors in [Log Locations: Build and Deploy Logs](https://devdocs.magento.com/cloud/project/log-locations.html#build-and-deploy-logs). Proceed to [Step 5](#step-5).

+++

## Step 5

+++**Error code reported?**

a. YES – Proceed to [Step 6](#step-6).  
b. NO – Proceed to [Step 7](#step-7).

+++

## Step 6

+++**403 Forbidden?**

a. YES – Proceed to [Step 15.](#step-15)  
b. NO – Proceed to [Step 8](#step-8).

+++

## Step 7

+++**Are cron jobs currently running?**

a. YES – Log in by ssh on the integration branch (e.g., primary). Kill and unlock cron jobs. This will kill cron jobs and reset the status. Run `php vendor/bin/ece-tools cron:kill` and then `php vendor/bin/ece-tools cron:unlock`. If you were in the process of merging one environment into another, check both environments for running crons.  
b. NO – Proceed to [Step 16.](#step-16)

+++

## Step 8

+++**Unable to upload application to the remote cluster error?**

a. YES – Proceed to [Step 9](#step-9).  
b. NO – Proceed to [Step 10.](#step-10)

+++

## Step 9

+++**Available storage okay?**

a. YES – Proceed with [Step 10](#step-10).  
b. NO – Review [Manage disk space](https://devdocs.magento.com/cloud/project/manage-disk-space.html).

+++

## Step 10

+++**_file could not be written Warning_?**

a. YES – Please [increase the disk value in .magento.app.yaml](https://devdocs.magento.com/cloud/project/manage-disk-space.html#application-disk-space) and redeploy. If this does not work, [submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251).  
b. NO – Proceed with [Step 11](#step-11).

+++

## Step 11

+++**Environment redeployment failed error?**

a. YES – Proceed with [Step 12](#step-12).  
b. NO – Proceed with [Step 7](#step-7).

+++

## Step 12

+++**Elasticsearch being upgraded or deployed?**

a. YES – Elasticsearch failed upgrade steps. Refer to [Elasticsearch software compatibility](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html). If the Elasticsearch upgrade still doesn't work, [submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251). **Note**: On Adobe Commerce on cloud infrastructure, please be aware that service upgrades cannot be pushed to the production environment without 48 business hours' notice to our infrastructure team. This is required as we need to ensure that we have an infrastructure support engineer available to update your configuration within the desired timeframe with minimal downtime to your production environment. So 48 hours prior to when your changes need to be on production, [submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251) detailing your required service upgrade and stating the time when you want the upgrade process to start.  
b. NO – Proceed to [Step 13](#step-13).

+++

## Step 13

+++**File system out of inodes or space?**

a. YES – See [Manage disk space](https://devdocs.magento.com/cloud/project/manage-disk-space.html).  
b. NO – Proceed to [Step 14](#step-14).

+++

## Step 14

+++**Error about Elasticseach versions?**

a. YES – Proceed to [Step 15](#step-15).  
b. NO – Proceed to [Step 20](#step-20).

+++

## Step 15

+++**Composer config correct?**

a. YES – Proceed to [Step 9](#step-9).  
b. NO – Review [Composer Troubleshooter webpage](https://getcomposer.org/doc/articles/troubleshooting.md).

+++

## Step 16

+++**Long running processes(es)?**

a. YES – Identify long running processes and then kill processes:
1. Run the following command in the terminal: `ps aufx`.
1. Locate the PID of the long-running process.
1. Terminate the process using `kill -9 <PID>`.

Monitor deployments for reoccurrence.  

b. NO – Proceed to [Step 17](#step-17).

+++

## Step 17

+++**Post hook failure/hang?**

a. YES – Database: [Free disk space](https://devdocs.magento.com/cloud/project/manage-disk-space.html#allocating-disk-space), corruption, incomplete/corrupted tables.  
b. NO – Proceed to [Step 18](#step-18).

+++

## Step 18

+++**Using third-party extensions?**

a. YES – Try [Disabling the third-party extensions](https://devdocs.magento.com/cloud/howtos/install-components.html#manage-extensions) and running the deployment (to see if they are the cause of the problem), especially if there are extension names in any errors.  
b. NO – Proceed to [Step 19](#step-19).

+++

## Step 19

+++**Long running queries?**

[Check slow query log and MySQL show processlist](https://support.magento.com/hc/en-us/articles/360030903091). 

a. YES – Kill any long running queries. Review [MySQL Kill Syntax.](https://dev.mysql.com/doc/refman/8.0/en/kill.html)  
b. NO – [Submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251).

+++

## Step 20

+++**Downgrading Elasticsearch versions?**

a. YES – Can't be done through configuration. [Submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251).  
b. NO – [Submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251).

[Back to Step 1](#step-1)
