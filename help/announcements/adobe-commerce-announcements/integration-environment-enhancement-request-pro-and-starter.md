---
title: Integration Environment enhancement request - Pro and Starter
description: If you are an Adobe Commerce on cloud infrastructure Pro plan architecture customer and currently use the standard-sized Integration Environments, or you are an Adobe Commerce on cloud infrastructure Starter plan architecture customer and currently use the standard sized Staging Environment and would like more power, you can request an upgrade to Enhanced Integration Environments, which provide roughly four times the performance. This article separates instructions for Pro customers from Starter customers.
exl-id: c49b049b-efb8-412f-b27d-a89f8a758d85
feature: Integration
role: Admin
---
# Integration Environment enhancement request - Pro and Starter

If you are an Adobe Commerce on cloud infrastructure Pro plan architecture customer and currently use the standard-sized Integration Environments, or you are an Adobe Commerce on cloud infrastructure Starter plan architecture customer and currently use the standard sized Staging Environment and would like more power, you can request an upgrade to Enhanced Integration Environments, which provide roughly four times the performance. This article separates instructions for Pro customers from Starter customers.

>[!NOTE] 
> Upgrading to Enhanced Integration may not address all performance issues as it would depend on the total resource requirements of your installation, including third-party integrations or customizations.
>
> You also need to make sure that you are following the best practices for best performance in the integration environment, and even that may not be an end-all solution. Refer to the following documentation for guidance, [Pro Architecture](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/pro-architecture#integration-environment) and [Starter Architecture](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/starter-architecture#staging-environment) in the Commerce on Cloud Infrastructure Guide.

## Pro

1. If you are on Pro, to upgrade, you must reduce the number of Integration branches to two (**the main Integration branch is included in the total**). **Note: Do not count the primary branch in this total. The primary branch is not considered an integration branch.** Follow the steps in [Manage branches with the Cloud Console](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/console-branches.html) in our developer documentation.
1. The merchant needs to [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) requesting an Upgrade to Enhanced Integration Environments, using the contact reason "*Request a cloud configuration change*".
1. Adobe Customer Engineering team confirms the number of Integration Environments and begins the change.
1. The merchant will be notified in the ticket when the upgrade is complete.
1. The merchant redeploys the Integration Environments. Follow the steps in [Merge a branch](https://devdocs.magento.com/cloud/env/environments-start.html#merge) in our developer documentation. *Note*: The deployment happens automatically when you run: <pre>git push origin <branch-name></pre>

Increased performance indicates a successful upgrade to Enhanced Integration Environments.

 **Notes**:

* The standard size and enhanced size are the only two sizes available.
* All the Integration Environments for a given store are the same size &ndash;  they cannot be sized independently.
* If you need more than two of the Enhanced Integration Environments, please consult your Adobe Account Team.

## Starter

1. Starter plans can't have any Integration branches: merchants must delete the Integration environments and leave only the Staging environment. Follow the steps in [Manage branches with the Cloud Console](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/console-branches.html) in our developer documentation. The number of environments available will be reduced to allow a maximum of one Integration Environment.
1. The merchant needs to [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) requesting an Upgrade to Enhanced Integration Environments, using the contact reason *"Request a cloud configuration change"* &ndash;  **your Staging environment is a named Integration Environment**.
1. Adobe Customer Engineering team confirms the number of Integration Environments and begins the change.
1. The merchant will be notified in the ticket when the upgrade is complete.
1. The merchant redeploys the Integration Environments. Follow the steps in [Merge a branch](https://devdocs.magento.com/cloud/env/environments-start.html#merge) in our developer documentation. *Note*: The deployment happens automatically when you run: <pre>git push origin <branch-name></pre>

Increased performance indicates a successful upgrade to Enhanced Integration Environments.

 **Notes**:

* The standard size and enhanced size are the only two sizes available.
* All the Integration Environments for a given store are the same size &ndash;  they cannot be sized independently.
* If you need Integration Environments beyond Staging, please consult your Adobe Account Team.
* In case the purchase is made after 17th September 2020, this enhancement won't be applicable due to enlarged Integration Environments.
