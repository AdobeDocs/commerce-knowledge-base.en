---
title: Adobe Commerce site down troubleshooter
description: Click on each question to reveal the answer details in each step of the troubleshooter.
exl-id: 10a2313e-cc82-4ffc-9247-624884f3e165
feature: Support
role: Developer
---
# Adobe Commerce site down troubleshooter

Click on each question to reveal the answer details in each step of the troubleshooter.

>[!NOTE]
>
>Before creating a [Support Ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide?lang=en#support-cases), check the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) to see if your issue is already listed

## Step 1 {#step-1}

+++**Does <https://status.adobe.com> show any issues?**

a. YES – If you checked [Adobe Commerce Status](https://status.adobe.com/cloud/experience_cloud), and it showed an issue, open a [Support Ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-cases) for further investigation.  
b. NO – If you checked [Adobe Commerce Status](https://status.adobe.com/cloud/experience_cloud), and it did not show an issue, proceed to [Step 2](#step-2).

+++

## Step 2 {#step-2}

+++**Does http://status.fastly.com show any issues?**

a. YES – If you checked [[!DNL Fastly] Status](https://status.fastly.com/) and it showed an issue, open a [Support Ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-cases) for further investigation.  
b. NO – If you checked [[!DNL Fastly] Status](https://status.fastly.com/) and it did not show an issue, proceed to [Step 3](#step-3).

+++

## Step 3 {#step-3}

+++**Check your website in a web browser. Do you get a 200 (OK) code?**

To check error codes in **Firefox**: Click the **Open Menu** icon > **Web Developer** > **Toggle Tools** > **Network** tab > **All** filter > **Status** column. To check error codes in **Chrome**: Click the **Open Menu** icon > **More Tools** > **Developer Tools** > **Network** tab > **All** filter > **Status** column.

a. YES – Open a [Support Ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-cases) for further investigation.  
b. NO – Proceed to [Step 4](#step-4).

+++

## Step 4 {#step-4}

+++**Which website error code did you receive?**

a. Error Code 500 – Check log of `/var/log/platform/`. If this data does not present the issue to you, you can open a [Support Ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-cases) and include the troubleshooting information you have so far for further investigation.

b. Error Code 503 – Check log of `var/reports`. If this data does not present the issue to you, you can open a [Support Ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-cases) and include the troubleshooting information you have so far for further investigation.

c. Error Code 404 - Run the following query: `SELECT f.flag_data->>'$.current_version' as flag_version, (su.id IS NOT NULL) as update_exists FROM flag f LEFT JOIN staging_update su ON su.id = f.flag_data->>'$.current_version' WHERE flag_code = 'staging';` If the query returns a table, where `update_exists` value is "0", refer to the [Error 404 on all pages, storefront and Admin, due to Content Staging issue](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/site-down-or-unresponsive/error-404-on-all-pages-due-to-content-staging-issue) article. In all other cases proceed to [Step 5](#step-5).

d. Other Error Codes – Proceed to [Step 5](#step-5).

+++

## Step 5 {#step-5}

+++**Is your site slow, or having high server load, high CPU load, slow request processing, or outages in [!DNL MySQL] or Redis?**

a. YES – Proceed with steps for [Checking for DDOS attacks from CLI](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/checking-for-ddos-attack-from-cli).  
b. NO – Check logs of `/var/log/exception.log` and `/var/log/deploy.log`, and if this data does not present the issue to you, proceed to [Step 6](#step-6).

+++

## Step 6 {#step-6}

+++**Do you have deployment errors or deployment failure?**

a. YES – Proceed to [Step 13](#step-13).  
b. NO – Proceed to [Step 7](#step-7).

+++

## Step 7 {#step-7}

+++**Do you have Elasticsearch errors?**

a. YES – Proceed with steps for [checking Elasticsearch](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/search/configure-search-engine).
b. NO – Proceed to [Step 8](#step-8).

+++

## Step 8 {#step-8}

+++**Was your [!DNL MySQL] database having slow queries or incorrect queries?**

a. YES – Proceed with [Checking slow queries and Processes taking too long in [!DNL MySQL]](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/database/checking-slow-queries-and-processes-mysql) and checking your query structure in this [[!DNL MySQL] query tutorial](https://dev.mysql.com/doc/refman/5.5/en/entering-queries.html).  
b. NO – Proceed to [Step 9](#step-9).

+++

## Step 9 {#step-9}

+++**Is your static content not available?**

a. YES – Proceed with consulting the [Checking static content](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/static-content-deployment) article.  
b. NO – Proceed to [Step 10](#step-10).

+++

## Step 10 {#step-10}

+++**Do you see PHP Fatal Errors in your logs?**

a. YES – Proceed with consulting [Common PHP Fatal Errors and solutions](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/common-php-fatal-errors-and-solutions).  
b. NO – Proceed to [Step 11](#step-11).

+++

## Step 11 {#step-11}

+++**Are you seeing Redis errors?**

a. YES – Proceed with steps to [verify [!DNL Redis] is running](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cache/redis/redis-session#verify-redis-connection) and for [[!DNL Redis] troubleshooting](https://redis.io/topics/problems).  
b. NO – Proceed to [Step 12](#step-12).

+++

## Step 12 {#step-12}

+++**Are you seeing Indexer errors?**

a. YES – If your Index is locked by another process, consult [Index is locked by another process](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/index-is-locked-by-another-process). If you have other Indexer errors, please open a [Support Ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-cases) for further investigation.  
b. NO – Open a [Support Ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-cases) for further investigation.

+++

## Step 13 {#step-13}

+++**Do you have issues with your custom module(s)?**

a. YES – Proceed to consult [General custom module troubleshooting help](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/general-custom-module-troubleshooting-help).  
b. NO – Proceed to [Step 14](#step-14).

+++

## Step 14 {#step-14}

+++**Do you have post-hook failures?**

a. YES – Proceed with checking your [!DNL MySQL] error in this [[!DNL MySQL] server error message reference](https://dev.mysql.com/doc/mysql-errors/5.7/en/server-error-reference.html).  
b. NO – Proceed to [Step 15](#step-15).

+++

## Step 15 {#step-15}

+++**Do you have issues with composer patches?**

a. YES – Proceed to consulting [Applying a patch takes your site down](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/site-down-or-unresponsive/applying-a-patch-takes-your-site-down).  
b. NO – Proceed to [Step 16](#step-16).

+++

## Step 16 {#step-16}

+++**Do you have SQL database errors?**

a. YES – Proceed with checking your [!DNL MySQL] error in this [[!DNL MySQL] server error message reference](https://dev.mysql.com/doc/mysql-errors/5.7/en/server-error-reference.html).  
b. NO – Proceed to [Step 17](#step-17).

+++

## Step 17 {#step-17}

+++**Do you have [!DNL MySQL] database dead locks or an unresponsive [!DNL MySQL] database?**

a. YES – Proceed with checking for [!DNL MySQL] deadlocks in this [Deadlocks in [!DNL MySQL]](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/database/deadlocks-in-mysql) article.  
b. NO – Open a [Support Ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-cases) for further investigation.

+++

[Back to Step 1](#step-1)

Click [HERE](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/site-down-or-unresponsive/site-down-troubleshooting-diagram) to see the Site Down Troubleshooting Flowchart.

## Related reading

[Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
