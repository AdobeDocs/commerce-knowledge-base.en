---
title: New domain is redirecting to default domain
description: This article provides a fix for the issue where the new domain is redirecting to the default domain in existing environment or another environment.
---
# New domain is redirecting to default domain

This article provides a fix for the issue when where the new domain is redirecting to the default domain in existing environment or another environment.

## Affected versions

* Adobe Commerce on cloud pro infrastructure (all versions)

## Issue

The new domain is redirecting to the default domain in the current environment or the default domain of another environment.

## Cause

It happens when the Magento Variables are not updated after adding a new domain or the wrong Fastly service has been configured in the environment.

## Solution

1. If the domain is redirecting within the same environment, make sure that you have configured the [Magento Variables](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure-store/multiple-sites.html#modify-variables).
1. If the domain is redirecting to another environment, check whether you have configured the correct Fastly service by running the following command: `bin/magento fastly:config:get -s`.

>[!NOTE]
>
>You can find the [!DNL Fastly] API credentials by logging in to each environment (Staging/Production) and checking the `/mnt/shared/fastly_tokens.txt` file. For more information, see [configure [!DNL Fastly] services](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration.html) in our developer documentation.

If both 




