---
title: Sync data and files Production to Staging or Staging to Integration
description: This article explains how to synchronize your Production environment down to Staging on Adobe Commerce on cloud infrastructure; this is not possible.
exl-id: e3d001d1-1b2a-41b5-9b4a-00e53dc9d001
feature: Integration, Build
---
# Sync data and files Production to Staging or Staging to Integration

This article explains how to synchronize your Production environment down to Staging on Adobe Commerce on cloud infrastructure; this is not possible via the user interface or the Magento-cloud CLI.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.3.x, 2.4.x

## To sync data from one environment to another

To sync the data, you must manually dump the database from the source environment. To transfer data to another environment, you must then upload the source dump to the target environment and import it. For more information, see [Import Adobe Commerce Code into a Cloud project > Import Adobe Commerce database](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/deploy/staging-production) in our developer documentation.

For Adobe Commerce on cloud infrastructure Pro plan architecture, you can also sync from Staging and Production to your Integration master branch. This sync only pulls and pushes code, not data. To sync data, you will need to dump the database data and push it to another environment's database.

>[!WARNING]
>
>Syncing of the database cannot be done in the Pro Staging and Production clusters.

## To sync files from one environment to another

To sync files from one environment to another, use the `rsync` command. For more information, see [Deploy code and migrate static files and data > Migrate files using rsync](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/deploy/staging-production#migrate-files-using-rsync) in our developer documentation.

>[!NOTE]
>
>If you want to sync the code from Integration to Staging, you must do it from the Integration branch. For steps, see [Sync from the environment’s parent](/docs/commerce-cloud-service/user-guide/project/console-branches.html#sync-an-environment) in our developer documentation.
