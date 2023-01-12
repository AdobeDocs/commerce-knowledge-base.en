---
title: Monitoring fact sheet for Adobe Commerce on cloud pro infrastructure
description: Monitoring provides visibility into the overall health of Adobe Commerce powered by Adobe and is
exl-id: 01342d8d-2123-4455-b1a5-a08a5805b046
---

# Monitoring fact sheet for Adobe Commerce on cloud pro infrastructure

Monitoring provides visibility into the overall health of Adobe Commerce and is instrumented with various monitoring tools to track the health of critical parts of our underlying systems to deliver optimized performance on cloud.

This document provides information about the systems and subsystems being monitored, thresholds set on mission-critical parameters, and notifications.

Monitoring enables customers, system integrators, and Adobe’s internal teams to:

* Measure performance metrics, the health of individual sub-components, and the cloud platform layer.
* Analyze Adobe Commerce site performance.
* Troubleshoot problems such as service availability, insufficient disk space, etc.

## Problem troubleshooting and resolution

Adobe Commerce instances generally contain custom code and configurations. Adobe does not support or resolve issues with custom code and configurations. Adobe does help customers troubleshoot and identify issues in our knowledge base and provide recommended solutions and best practices for prevention and resolution. We encourage our customers and partners to use the tables below to understand what is monitored, who is responsible for resolution.

When notifications are triggered, Adobe Commerce support team will triage the issue. As part of the triage, error logs, and other resources are analyzed. Based on the triage, additional Zendesk support tickets are created either to customer or partner (in case of custom updates) or to Adobe’s internal teams to resolve the issue.
<!-- is the above paragraph problematic because it implies that notifications are triggering Zendesk support tickets that are getting triaged? -->

 Our [Managed Alerts](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce.html) can help you take action before you notice slow response times or an outage.

## Adobe Commerce: default monitoring

The below events are monitored and the Adobe Commerce team (including non-Adobe Managed Services (AMS)/Premier support) take necessary steps to resolve and communicate issues identified.

## Site availability monitoring

 |  Site availability  | Description |
 |------------|------------|
 | **Monitoring goal** | To track site availability |
 | **Instrumented on** | Single URL selected for high SLA. |
 | **Description** | Site availability is determined based on the thresholds configured around the metric. Notification of site outage gets triggered if the check fails for 10 minutes and there is no active deployment in progress.|
 | **Notification recipient** | Customer / Partner and Adobe. |
 | **Action by Adobe** | Responsible for triaging and fixing if the issue is on Adobe commerce platform.|
 | **Action by customer** | Responsible for fixing the issue if caused by changes introduced by customer/partner. For troubleshooting, please refer to: [Site Down Troubleshooter](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/site-down-or-unresponsive/magento-site-down-troubleshooter.html). |

## Diskspace monitoring

| Diskspace monitoring    | Description |
|------------|------------|
|Monitoring goal |To track diskspace availability.|
| Instrumented on | Host system running containers with services or services directly. Services include Galera, MariaDB, Solr, Redis, Elasticsearch, Nginx, Memcached and deployment infrastructure.|
| Metric | Free diskspace is monitored every minute on the host. Warning is raised if just 5% or 2GB free space is left. Critical threshold is set at the remaining free space is 2% or 1GB|
| Description | Notification is sent based on the thresholds configured around free diskspace for the host. |
| Notification recipient | Internal and [Managed alerts](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce.html) are created within Adobe and for the customer. |
| Action by Adobe | Responsible for triaging and fixing if the issue is on Adobe Commerce platform. |
| Action by customer | Responsible for fixing the issue if caused by changes introduced by customer or partner.  For troubleshooting, please refer to: <ul><li>[Managed alerts for Adobe Commerce: disk warning alert](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce-disk-warning-alert.html)</li><li>[Managed alerts for Adobe Commerce: disk critical alert](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce-disk-critical-alert.html) </li></ul> |

## CPU monitoring

| CPU monitoring   | Description |
|------------|------------|
|Monitoring goal |To track CPU availability.|
| Instrumented on | |
| Metric | CPU storage is monitored ...|
| Description | Notification is sent based on the thresholds configured around free CPU .... |
| Notification recipient | Internal and [Managed alerts](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce.html) are created within Adobe and for the customer. |
| Action by Adobe | ... |
| Action by customer | Responsible for fixing the issue if caused by changes introduced by customer or partner.  For troubleshooting, please refer to: <ul><li>[Managed alerts for Adobe Commerce: CPU warning alert](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce-cpu-warning-alert.html)</li><li>[Managed alerts on Adobe Commerce: CPU critical alert](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-on-magento-commerce-cpu-critical-alert.html) </li></ul> |
