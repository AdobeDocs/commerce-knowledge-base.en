---
title: General custom module troubleshooting help
description: This article talks about general tools to help in troubleshooting custom modules in Adobe Commerce.
exl-id: c6603a2b-dc98-4022-ab29-c081c2b07415
feature: Extensions
role: Developer
---
# General custom module troubleshooting help

This article talks about general tools to help in troubleshooting custom modules in Adobe Commerce.

## Issue

If you realize there is an issue with the features from your custom module, and you get no obvious error messages that state the issue, then you will want to consult your instance's logs.

## Solution

Check the logs to see if there are entries with custom module's name in the error.  Depending on the errors involved, the solution may present itself, or you may need to include your helpful Adobe Commerce log information if you want to open a [Support Ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket). See the following paragraphs for the info about logs' location and possible solutions.

### Adobe Commerce (all deployment methods), Magento Open Source, all 2.X versions

1. Logs location is placed at [Adobe Commerce on cloud infrastructure Pro plan architecture logs](/help/how-to/general/log-locations-directories-for-pro-plan-integration-staging-production.md) in our support knowledge base.
1. Depending on the errors you find, if you want to enable, disable, or uninstall a custom module, these articles detail those actions:
    * [Enable or disable modules](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/manage-modules) in our developer documentation.
    * [Uninstall modules](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/uninstall-modules) in our developer documentation.

### Adobe Commerce on cloud infrastructure, all versions

1. Logs locations: [Adobe Commerce on cloud infrastructure logs](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/test/log-locations) in our developer documentation.
1. Depending on the errors you find, if you want to enable, disable, or uninstall a custom module, these articles in our developer documentation detail those actions:
    * [Install, manage, and upgrade extensions](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure-store/extensions).
    * [Component deployment failure](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/deploy/recover-failed-deployment).

## Related reading

In our developer documentation:

* [Module overview](https://developer.adobe.com/commerce/php/architecture/modules/overview/)
* [Errors installing optional sample data](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/installation-and-upgrade/errors-installing-optional-sample-data)
* [Exception handling](https://developer.adobe.com/commerce/webapi/graphql/develop/exceptions/)
* [Exceptions during installation](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/installation-and-upgrade/exceptions-during-installation)
* [Run the Module Manager](https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/prepare/prerequisites)
* [Module configuration files](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/files/module-files)
* [Out of memory errors](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/installation-and-upgrade/out-of-memory-error-during-install-or-upgrade)
