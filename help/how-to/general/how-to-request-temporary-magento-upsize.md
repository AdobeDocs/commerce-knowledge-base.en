---
title: How to request temporary Adobe Commerce on cloud infrastructure upsize
description: If your organization is planning an online event in which you expect high traffic, or you suddenly find your site to be undergoing a high traffic event, you can file a [Support Ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) to request temporary additional cloud capacity for your Adobe Commerce on cloud infrastructure store.
exl-id: 561e2bdd-718a-45c1-8b6c-a0e3a6c8ad04
feature: Cloud, Iaas
---
# How to request temporary Adobe Commerce on cloud infrastructure upsize

If your organization is planning an online event in which you expect high traffic, or you suddenly find your site to be undergoing a high traffic event, you can file a [Support Ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) to request temporary additional cloud capacity for your Adobe Commerce on cloud infrastructure store.

>[!NOTE]
>
>48 business hours notice is required for non-emergency upsize requests. Upsizes for promotional campaigns are not considered emergencies unless the site is completely non-functional or receiving much higher traffic than anticipated and performance has been severely degraded.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all [supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf).

## How to identify high traffic events

In New Relic Alerts, you can use baseline alert conditions to define thresholds that adjust to the behavior of your data.

Baseline alerting is useful for creating alert conditions that:

* Only notify you when data is behaving abnormally.
* Dynamically adjust to changing data and trends, including daily or weekly trends.

In addition, baseline alerting works well with new applications when you do not yet have known behaviors.

Follow this link to learn more about New Relic [Anomaly detection with  applied Intelliegence](https://docs.newrelic.com/docs/alerts-applied-intelligence/applied-intelligence/anomaly-detection/anomaly-detection-applied-intelligence/).

If you receive an alert notification that suggests a high traffic event you may need to consider [submitting a Support Ticket](/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html?lang=en#submit-ticket) requesting additional capacity. Follow the below steps.

## How to monitor performance of your site

Adobe provides a set of New Relic alert policies for Adobe Commerce on cloud infrastructure Pro plan architecture and Adobe Commerce on cloud infrastructure Starter plan architecture Production environments to track the following key performance metrics:

* [Apdex score](https://docs.newrelic.com/docs/apm/new-relic-apm/apdex/apdex-measure-user-satisfaction)
* Error rate
* Disk space (available on Pro architecture Production environments only)

Based on industry best practices, these policies set thresholds for warning and critical conditions that affect performance. When your site experiences an infrastructure or application issue that triggers an alert threshold, New Relic sends alert notifications so that you can proactively address the issue. To use these policies, you must configure notification channels to receive the alert messages.

Follow this link to learn how to [configure performance-based alerts](/docs/commerce-cloud-service/user-guide/monitor/new-relic.html#monitor-performance-with-managed-alerts).

## Steps to request temporary upsize

To request temporary additional cloud capacity, submit a [/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket]Support Ticket at the Adobe Commerce Support Center with the following information:

>[!NOTE]
>
>The *Holiday Surge Request* choice is only an option between October and December months.

1. Select the [!DNL Adobe Commerce] product you need support for:
    * [!DNL Commerce Cloud]
    * [!DNL Commerce on Managed Service]

1. Complete the following fields:
    * **[!UICONTROL Case Title]**
    * **[!UICONTROLCase Description]** *(ensure these clearly describe the issue and context.)*

1. Select *Infrastructure Change Request* from the **[!UICONTROL Issue Reason]** dropdown menu.

1. Choose the **[!UICONTROL Environment]** from the dropdown menu.

1. Select the appropriate **[!UICONTROL Product Version]** from the dropdown menu.

1. Choose *Cloud Project Resize (vCPU)* from the **[!UICONTROL Which Infra Change you would like to do today]** dropdown menu.

1. **Select the [!UICONTROL Architecture]**:
    * *Default Architecture:* Select *Next Available Size* from the **Select the Size** dropdown menu.
    * *Scaled Architecture:* When selected, the screen changes to show two additional fields:
        * *Size for Web Node*
        * *Size for Service Node* *(enter the desired sizes for each node.)*

1. Enter the **[!UICONTROL From Date]** in UTC format (date and time).

1. Enter the **[!UICONTROL To Date]** in UTC format (date and time).

1. Provide **[!UICONTROL Project URL]** *(found under https://accounts.magento.cloud/, typically in the format `https://[REGION].magento.cloud/projects/PROJECT_ID`)*

1. Enter the **[!UICONTROL Project ID]**.

1. Provide **[!UICONTROL Affected URL]** *(must begin with `http://` or `https://`.)*

1. Select **[!UICONTROL Priority]**.

1. Select **[!UICONTROL Business Impact]**.

1. Confirm **[!UICONTROL Time Zone]** *(e.g., `(UTC-5:00) Indiana (East)`)*

1. Enter **[!UICONTROL Phone Number]** *(e.g., `+12015550123`)*

1. Click **[!UICONTROL Submit]** to finalize your support case.

>[!NOTE]
>
>Once the upsize is scheduled, an automated system will adjust the size of your cloud instance. You may not receive any ticket notification when the procedure is complete. You may use the Observation for Adobe Commerce tool to view your AWS or Azure instance types to [verify the change](/help/how-to/general/check-vcpu-using-observation-for-adobe-commerce.md).

## View the history of your upsizes

You can view the history of requested resizes by requesting the information from your **CSM (Customer Success Manager)**.
The following information is available for each resize request:

* **Size Start Date**: date of upsize request.
* **Size End Date**: date when the cluster was returned to the previous size.
* **vCPU Size**: the size of the cluster after the upsize.
* **Days Usage**: for how many days the cluster stayed upsized.
* **Period vCPU**: changed vCPU size by the number of days it was used. (for example, vCPU size 192 by 25 days equals 4,800).


## Related reading

* For insights, methods, and examples of how to measure and improve site performance, refer to the following in-depth articles in our support knowledge base:
    * [CPU allocation calculation for Adobe Commerce on cloud](/docs/commerce-knowledge-base/kb/how-to/magento-commerce-cloud-cpu-allocation-calculation.html)
    * [Check if upsize for host's instances is needed for Adobe Commerce on cloud](/docs/commerce-knowledge-base/kb/how-to/magento-commerce-cloud-check-if-upsize-for-hosts-instances-is-needed.html)
    * [Check host's CPU configuration for Adobe Commerce on cloud](/docs/commerce-knowledge-base/kb/how-to/magento-commerce-cloud-check-hosts-cpu-configuration.html)
* For information on how to identify outages, refer to [Identify and measure outages for Adobe Commerce on cloud](/docs/commerce-knowledge-base/kb/how-to/how-to-identify-outages.html) in our support knowledge base.
* For information on improving site performance to avoid the need for utilizing an increase in capacity, refer to these articles in our developer documentation:
    * [Image Sizing](/docs/commerce-admin/catalog/products/digital-assets/product-image-config.html#product-image-resizing)
    * [Full Page Caching](/docs/commerce-admin/systems/tools/cache-management.html#full-page-caching)
    * [ECE-Tools](/docs/commerce-cloud-service/user-guide/dev-tools/ece-tools/package-overview.html)
