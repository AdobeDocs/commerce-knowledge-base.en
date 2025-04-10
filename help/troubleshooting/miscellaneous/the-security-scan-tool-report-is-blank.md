---
title: The Security Scan Tool report is blank
description: This article provides a fix for the issue where the Security Scan Tool shows a blank page instead of the actual report. To resolve it, you might need to add the IPs used by the Tool to the firewall AllowList.
exl-id: e5f7f8c6-2dd3-44e3-8d19-f1f38d06dd6c
feature: Compliance, Security
role: Developer
---
# The Security Scan Tool report is blank

This article provides a fix for the issue where the Security Scan Tool shows a blank page instead of the actual report. To resolve it, you might need to add the IPs used by the Tool to the firewall AllowList.

## Affected products and versions:

* Adobe Commerce (all deployment methods) and Magento Open Source, All versions

## Issue

<u>Steps to reproduce</u>:

1. Configure the Security Scan Tool to check your website, as described in [Security Scan](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/security/security-scan) in our user guide.
1. In the Actions column, select **Run Scan**.

<u>Expected results</u>:

View the report completion notification and the ability to open the report.

<u>Actual results</u>:

No notification and no report available.

## Cause

This issue might appear because the Security Scan Tool was not able to reach your website. This means either the website is down and cannot be reached at all, or the Security Scan Tool is being blocked.

## Solution

Try to open your website.

* If the page loads successfully, you might need to add the IPs used by the Security Scan Tools to the firewall AllowList. The following IPs are used: 52.87.98.44, 34.196.167.176, 3.218.25.102 at ports 80 and 443.
* If the site doesn't load and returns the *"There has been an error processing your request"* message, check your website for possible errors.

## Related reading

* [Go live and launch](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/launch/overview) in our developer documentation.
* [Security Scan](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/security/security-scan) in our user guide.
