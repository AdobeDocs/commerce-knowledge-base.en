---
title: Check logs to troubleshoot 500 and 503 errors on Adobe Commerce
description: This article explains how to check the `access.log` and related logs to troubleshoot 503 and 500 errors, which can be caused by traffic or insufficient server resources. Viewing the `access.log` and related logs can provide information on what may be causing problems related to Adobe Commerce on cloud infrastructure.
exl-id: 47d7de6b-3e12-4e79-a5c1-c27a9196b99c
feature: Cloud, Logs
---
# Check logs to troubleshoot 500 and 503 errors on Adobe Commerce

This article explains how to check the `access.log` and related logs to troubleshoot 503 and 500 errors, which can be caused by traffic or insufficient server resources. Viewing the `access.log` and related logs can provide information on what may be causing problems related to Adobe Commerce on cloud infrastructure.

<!--
Bob - not in TOC
-->

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all [supported versions](https://experienceleague.adobe.com/docs/commerce-operations/release/planning/lifecycle-policy.html).

To view logs for these server errors, check the `access.log` on the web server, e.g., `<ip address>` `<timestamp>` `<request uri>` `<response code>` `<referer url>`

To check related logs:

1. Run the following command in the CLI if it is on the current day (for Adobe Commerce on cloud infrastructure Pro plan architecture). Or up to a certain point in the past (for Adobe Commerce on cloud infrastructure Starter plan architecture), since the duration of the logs' coverage is limited, and log rotation is not available: `grep -r "\" [50[0-9]" /path/to/access.log` If the error has occurred in the past run the following command in the CLI (Pro architecture only): `zgrep "\" 50[0-9]" /path/to/access.log.<rotation ID>.gz`
1. Then check the `exception.log` and `error.log` or the equivalent [rotated log](https://experienceleague.adobe.com/docs/commerce-operations/installation-guide/next-steps/configuration.html#log-rotation) (logs that are automatically rotated and compressed when they reach a certain file size) for the same timestamp to locate the potential error and see what might have been occurring to have caused it. Note: To check the `exception.log` and `error.log` run the above commands in the CLI but replace `access.log` with `exception.log` or `error.log`.

## Related reading

* See [View and manage logs](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/test/log-locations.html) in the *Adobe Commerce on Cloud Infrastructure Guide*.
* See [Troubleshooting 503 errors](/help/troubleshooting/miscellaneous/troubleshooting-503-errors.md) in our support knowledge base.