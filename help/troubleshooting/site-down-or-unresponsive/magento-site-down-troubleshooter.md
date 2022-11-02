---
labels: zendesk
title: Adobe Commerce site down troubleshooter
description: "Click on each question to reveal the answer details in each step of the troubleshooter."
---

# Adobe Commerce site down troubleshooter

Click on each question to reveal the answer details in each step of the troubleshooter.

## Step 1

+++**Does <https://status.adobe.com> show any issues?**

a. YES – If you checked [Adobe Magento Status](https://status.adobe.com/products/3350) and it showed an issue, open a [Support Ticket](https://support.magento.com/hc/en-us/articles/360019088251-Submit-a-support-ticket) for further investigation.  
b. NO – If you checked [Adobe Magento Status](https://status.adobe.com/products/3350) and it did not show an issue, proceed to [Step 2](#step-2).

+++

## Step 2

+++**Does http://status.fastly.com show any issues?**

a. YES – If you checked [Fastly Status](https://status.fastly.com/) and it showed an issue, open a [Support Ticket](https://support.magento.com/hc/en-us/articles/360019088251-Submit-a-support-ticket) for further investigation.  
b. NO – If you checked [Fastly Status](https://status.fastly.com/) and it did not show an issue, proceed to [Step 3](#step-3).

+++

## Step 3

+++**Check your website in a web browser. Do you get a 200 (OK) code?** 

To check error codes in **Firefox**: Click the **Open Menu** icon > **Web Developer** > **Toggle Tools** > **Network** tab > **All** filter > **Status** column. To check error codes in **Chrome**: Click the **Open Menu** icon > **More Tools** > **Developer Tools** > **Network** tab > **All** filter > **Status** column.

a. YES – Open a [Support Ticket](https://support.magento.com/hc/en-us/articles/360019088251-Submit-a-support-ticket) for further investigation.  
b. NO – Proceed to [Step 4](#step-4).

+++

## Step 4

+++**Which website error code did you receive?**

a. Error Code 500 – Check log of `/var/log/platform/`. If this data does not present the issue to you, you can open a [Support Ticket](https://support.magento.com/hc/en-us/articles/360019088251-Submit-a-support-ticket) and include the troubleshooting information you have so far for further investigation.

b. Error Code 503 – Check log of `var/reports`. If this data does not present the issue to you, you can open a [Support Ticket](https://support.magento.com/hc/en-us/articles/360019088251-Submit-a-support-ticket) and include the troubleshooting information you have so far for further investigation.

c. Error Code 404 - Run the following query: `SELECT f.flag_data->>'$.current_version' as flag_version, (su.id IS NOT NULL) as update_exists FROM flag f LEFT JOIN staging_update su ON su.id = f.flag_data->>'$.current_version' WHERE flag_code = 'staging';` If the query returns a table, where `update_exists` value is "0", refer to the [Error 404 on all pages, storefront and Admin, due to Content Staging issue](https://support.magento.com/hc/en-us/articles/360000262174) article. In all other cases proceed to [Step 5](#step-5).

d. Other Error Codes – Proceed to [Step 5](#step-5).

+++

## Step 5

+++**Is your site slow, or having high server load, high CPU load, slow request processing, or outages in MySQL or Redis?**

a. YES – Proceed with steps for [Checking for DDOS attacks from CLI](https://support.magento.com/hc/en-us/articles/360030941932).  
b. NO – Check logs of `/var/log/exception.log` and `/var/log/deploy.log`, and if this data does not present the issue to you, proceed to [Step 6](#step-6).

+++

## Step 6

+++**Do you have deployment errors or deployment failure?**

a. YES – Proceed to [Step 13](#step-13).  
b. NO – Proceed to [Step 7](#step-7).

+++

## Step 7

+++**Do you have Elasticsearch errors?**

a. YES – Proceed with steps for [checking Elasticsearch](https://devdocs.magento.com/guides/v2.3/config-guide/elasticsearch/configure-magento.html).  
b. NO – Proceed to [Step 8](#step-8).

+++

## Step 8

+++**Was your MySQL database having slow queries or incorrect queries?**

a. YES – Proceed with [Checking slow queries and Processes taking too long in MySQL](https://support.magento.com/hc/en-us/articles/360030903091) and checking your query structure in this [MySQL query tutorial](https://dev.mysql.com/doc/refman/5.5/en/entering-queries.html).  
b. NO – Proceed to [Step 9](#step-9).

+++

## Step 9

+++**Is your static content not available?**

a. YES – Proceed with consulting the [Checking static content](https://support.magento.com/hc/en-us/articles/360031624091) article.  
b. NO – Proceed to [Step 10](#step-10).

+++

## Step 10

+++**Do you see PHP Fatal Errors in your logs?**

a. YES – Proceed with consulting [Common PHP Fatal Errors and solutions](https://support.magento.com/hc/en-us/articles/360030568432).  
b. NO – Proceed to [Step 11](#step-11).

+++

## Step 11

+++**Are you seeing Redis errors?**

a. YES – Proceed with steps to [verify Redis is running](https://devdocs.magento.com/guides/v2.3/config-guide/redis/redis-session.html#redis-verify) and for [Redis troubleshooting](https://redis.io/topics/problems).  
b. NO – Proceed to [Step 12](#step-12).

+++

## Step 12

+++**Are you seeing Indexer errors?**

a. YES – If your Index is locked by another process, consult [Index is locked by another process](https://support.magento.com/hc/en-us/articles/360030683752). If you have other Indexer errors, please open a [Support Ticket](https://support.magento.com/hc/en-us/articles/360019088251-Submit-a-support-ticket) for further investigation.  
b. NO – Open a [Support Ticket](https://support.magento.com/hc/en-us/articles/360019088251-Submit-a-support-ticket) for further investigation.

+++

## Step 13

+++**Do you have issues with your custom module(s)?**

a. YES – Proceed to consult [General custom module troubleshooting help](https://support.magento.com/hc/en-us/articles/360031030751).  
b. NO – Proceed to [Step 14](#step-14).

+++

## Step 14

+++**Do you have post-hook failures?**

a. YES – Proceed with checking your MySQL error in this [MySQL server error message reference](https://dev.mysql.com/doc/mysql-errors/5.7/en/server-error-reference.html).  
b. NO – Proceed to [Step 15](#step-15).

+++

## Step 15

+++**Do you have issues with composer patches?**

a. YES – Proceed to consulting [Applying a patch takes your site down](https://support.magento.com/hc/en-us/articles/360030867871).  
b. NO – Proceed to [Step 16](#step-16).

+++

## Step 16

+++**Do you have SQL database errors?**

a. YES – Proceed with checking your MySQL error in this [MySQL server error message reference](https://dev.mysql.com/doc/mysql-errors/5.7/en/server-error-reference.html).  
b. NO – Proceed to [Step 17](#step-17).

+++

## Step 17

+++**Do you have MySQL database dead locks or an unresponsive MySQL database?**

a. YES – Proceed with checking for MySQL dead locks in this [Deadlocks in MySQL](https://support.magento.com/hc/en-us/articles/360031622211) article.  
b. NO – Open a [Support Ticket](https://support.magento.com/hc/en-us/articles/360019088251-Submit-a-support-ticket) for further investigation.

+++

[Back to Step 1](#step-1)

Click [HERE](https://support.magento.com/hc/en-us/articles/360031107111) to see the Site Down Troubleshooting Flowchart.