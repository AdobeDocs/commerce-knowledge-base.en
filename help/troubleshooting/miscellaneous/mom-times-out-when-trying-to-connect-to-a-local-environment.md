---
title: Magento Order Management System (OMS) for Adobe Commerce times out
description: This article provides a solution for the issue where the Magento Order Management System (OMS) for Adobe Commerce cannot register the locally installed micro-service with MOM using ngrok, because MOM times out when trying to callback.
exl-id: 19149d8c-ea24-46fb-8815-9f637afe46ca
feature: System
role: Developer
---
# Magento Order Management System (OMS) for Adobe Commerce times out

This article provides a solution for the issue where the Magento Order Management System (OMS) for Adobe Commerce cannot register the locally installed micro-service with MOM using ngrok, because MOM times out when trying to callback.

## Affected products and versions

* Adobe Commerce 2.3.1
* OMS
* ngrok

>[!WARNING]
>
>Disclaimer: Adobe Commerce does not recommend or endorse any particular tool for establishing tunnels. The preceding are suggestions only. For more information, consult the [ngrok documentation](https://ngrok.com/docs).

## Issue

 <u>Steps to reproduce</u>

1. Install Adobe Commerce on your local environment.
1. Set up ngrok to create a tunnel to expose your local server.
1. Try [connecting to OMS](https://commerce-docs.github.io/oms-documentation-archive/integration/connector/setup-tutorial/).

 <u>Expected result</u>

Connection established successfully.

 <u>Actual result</u>

MCOM seems to timeout when trying to callback to the ngrok URL.

## Cause

One of the possible reasons for the timeout is that servers are located geographically too far away, and connection takes too much time.

## Solution

Add a parameter specifying your region when starting ngrok. Like the following:

```bash
./ngrok http 80 -region eu
```

The default region is US. See [all possible values](https://ngrok.com/docs#config_region).
