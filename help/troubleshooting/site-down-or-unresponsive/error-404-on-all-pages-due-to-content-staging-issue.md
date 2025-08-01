---
title: Error 404 on all pages due to Content Staging issue
description: This article provides a fix for the Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure issue where you get a 404 error when accessing any storefront page or the [!UICONTROL Commerce Admin].
exl-id: 62d8ba6e-8550-4e1e-8e8d-8f319c92778a
feature: CMS, Catalog Management, Categories, Page Content, Staging
role: Developer
---
# Error 404 on all pages due to Content Staging issue

This article provides a fix for the Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure issue where you get a 404 error when accessing any storefront page or the [!UICONTROL Commerce Admin].

## Affected products and versions

* Adobe Commerce on-premises 2.2.x, 2.3.x
* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x

## Issue

>[!NOTE]
>
>This article doesn't apply to the situation in which you get a 404 error when trying to [preview the staging update](https://experienceleague.adobe.com/en/docs/commerce-admin/content-design/guide-overview#preview-the-scheduled-change). If you run into that issue, please open a [support ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-case).

Accessing any storefront page or the Admin results in the 404 error (the "Whoops, our bad..." page) after performing operations with scheduled updates for store content assets using [Content Staging](https://experienceleague.adobe.com/docs/commerce-admin/content-design/staging/content-staging.html) (updates for store content assets scheduled using the [Magento\_Staging module](https://developer.adobe.com/commerce/php/module-reference/)). For example, you may have deleted a Product with a scheduled update or removed the end date for the scheduled update.

A store content asset includes:

* Product
* Category
* Catalog Price Rule
* Cart Price Rule
* CMS Page
* CMS Block
* Widget

Some scenarios are discussed in the Cause section below.

## Cause

The `flag` table in the database (DB) contains invalid links to the `staging_update` table.

The problem is related to Content Staging. Below are two particular scenarios; please note there might be more situations that trigger the issue.

 **Scenario 1:** Deleting a store content asset which:

* has an update scheduled with Content Staging
* the update has an end date (meaning the expiry date after which the updated asset reverts to its previous version)
* the end date of the update is in the past

At the same time, the issue might not occur if a deleted asset has no end date for the scheduled update.

 **Scenario 2:** Removing the end date/time of a scheduled update.

### Identify if your issue is related

To identify if the issue you are experiencing is the one described in this article, run the following DB query:

```sql
   SELECT f.flag_data >'$.current_version' as flag_version, (su.id IS NOT NULL) as update_exists
   -> FROM flag f
   -> LEFT JOIN staging_update su
   -> ON su.id = f.flag_data >'$.current_version'
   -> WHERE flag_code = 'staging';
```

If the query returns a table where `update_exists` value is "0", then an invalid link to the `staging_update` table exists in your database, and the steps described in the [Solution section](#solution) will help to solve the issue. The following is an example of the query result with `update_exists` value equal to "0":

![update_exists_0.png](assets/update_exists_0.png)

If the query returns a table where `update_exists` value is "1" or an empty result, it means your issue is not related to staging updates. The following is an example of the query result with `update_exists` value equal to "1":

![updates_exist_1.png](assets/updates_exist_1.png)

In this case, you might refer to the [Site Down Troubleshooter](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27152) for troubleshooting ideas.

## Solution

1. Run the following query to delete the invalid link to the `staging_update` table:

   ```sql
   DELETE FROM flag WHERE flag_code = 'staging';
   ```

1. Wait for the [!DNL cron] job to run (runs in up to five minutes if set up properly) or run it manually if you do not have [!DNL cron] set up.

The problem should be solved straight after fixing the invalid link. If the problem persists, [submit a support ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-case).

## Related reading

[Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
