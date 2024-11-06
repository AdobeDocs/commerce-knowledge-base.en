---
title: 404 not found error when accessing Web Setup Wizard via Admin panel
description: This article provides a solution for when you experience a 404 not found error when trying to access the Web Setup Wizard via the admin panel.
exl-id: 1b89da58-c872-481b-b2a0-aa48db8223db
feature: Admin Workspace, Cloud, Paas
role: Developer
---
# 404 not found error when accessing Web Setup Wizard via Admin panel

This article provides a solution for when you experience a 404 not found error when trying to access the Web Setup Wizard via the admin panel.

## Affected products and versions

* The Web Setup Wizard functionality was deprecated in Adobe Commerce (all deployment methods) 2.3.6 and removed in 2.4.0.

## Issue

When installing an extension using Web Setup Wizard a 404 page displays.

<u>Steps to reproduce</u>:

Merchant clicks the Web Setup Wizard to install new module/integration.

<u>Expected result</u>:

Module/integration installs.

<u>Actual result</u>:

A 404 error displays.

## Cause

The Web Setup Wizard has been disabled for all Adobe Commerce on cloud infrastructure instances - it is not possible to enable it. Extensions have to be installed through composer.

## Solution

This feature is disabled on Adobe Commerce on cloud infrastructure.

See [Install, manage, and upgrade extensions](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure-store/extensions) in our developer documentation for information on how to perform updates or install external modules for Adobe Commerce on our cloud infrastructure.
See [Quick start install](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/composer) in our developer documentation for information on how to perform updates or install external modules for Adobe Commerce on-premises.

## Related reading

* See [Install an extension](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure-store/extensions#install-an-extension) in our developer documentation.
