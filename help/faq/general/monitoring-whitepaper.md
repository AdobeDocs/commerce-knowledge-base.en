---
title: Monitoring fact sheet for Adobe Commerce on cloud pro infrastructure
description: This document provides information about Adobe Commerce infrastructure monitoring and notifications.
exl-id: 01342d8d-2123-4455-b1a5-a08a5805b046
---

# Monitoring fact sheet for Adobe Commerce on cloud pro infrastructure

This document provides information about Adobe Commerce infrastructure monitoring and notifications.

Monitoring enables merchants, system integrators, and Adobe's internal teams to troubleshoot service availability and insufficient disk space.

## Problem troubleshooting and resolution

Adobe Commerce instances generally contain custom code and configurations. Adobe does not support or resolve issues with custom code and configurations. Adobe does help merchants troubleshoot and identify issues in our knowledge base and provide recommended solutions and best practices for prevention and resolution. We encourage merchants and partners to use the tables below to understand what is monitored and who is responsible for resolution.

When notifications are triggered, Adobe Commerce support team will triage the issue. As part of the triage, error logs, and other resources are analyzed. Based on the triage, additional Zendesk support tickets are created either to merchants or partner (in case of custom updates) or to Adobe's internal teams to resolve the issue.

## Adobe Commerce: default monitoring

The below events are monitored and the Adobe Commerce team (including non-Adobe Managed Services (AMS)/Premier support) take necessary steps to resolve and communicate issues identified.

## Site availability monitoring

 |  Site availability  | Description |
 |------------|------------|
 | **Monitoring goal** | To track site availability. |
 | **Instrumented on** | Single URL selected for high SLA. |
 | **Description** | Site availability is determined based on the thresholds configured around the metric. Notification of site outage gets triggered if the check fails for 10 minutes and there is no active deployment in progress.|
 | **Notification recipient** | Merchant/Partner and Adobe. |
 | **Action by Adobe** | Responsible for triaging and fixing if the issue is on Adobe commerce infrastructure.|
 | **Action by merchant** | Responsible for fixing the issue if caused by changes or custom code introduced by merchant/partner. For troubleshooting, please refer to: [Site Down Troubleshooter](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/site-down-or-unresponsive/magento-site-down-troubleshooter.html). |

## Diskspace monitoring

| Diskspace monitoring    | Description |
|------------|------------|
|Monitoring goal |To track diskspace usage.|
| Instrumented on | MySQL disk and Media disk partitions.|
| Metric | Free diskspace is monitored every minute on the host. Warning is raised if just 5% or 2GB free space is left. Critical threshold set at the remaining free space is 2% or 1GB.|
| Description | Notification is sent based on the thresholds configured around free diskspace for the host. Additional disk space is automatically added one time to the relevant mount (MySQL or media) to prevent a site outage and to give the merchant time to clear disk space and/or to identify and resolve any code or logs causing rapid disk usage increase.|
| Notification recipient | Merchant/Partner and Adobe. |
| Action by Adobe | Automatically raise support ticket and additional disk space is automatically added to the relevant mount (MySQL or media) to prevent a site outage. |
| Action by merchant | To receive ongoing warning level disk space alerts, please refer to: <ul><li>[Managed alerts for Adobe Commerce: disk warning alert](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce-disk-warning-alert.html)</li><li>[Managed alerts for Adobe Commerce: disk critical alert](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce-disk-critical-alert.html) </li></ul> |

