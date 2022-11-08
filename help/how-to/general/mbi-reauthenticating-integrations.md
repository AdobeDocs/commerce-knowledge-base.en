---
title: 'MBI: Re-authenticating integrations'
description: This article provides solutions for re-authorizing an integration to grant Magento Business Intelligence (MBI) the required privileges to pull data from a third-party service. Re-authorization is required when these privileges are revoked.
exl-id: c608d6f9-64a5-44f8-9d7b-9a85a2668775
---
# MBI: Re-authenticating integrations

This article provides solutions for re-authorizing an integration to grant Magento Business Intelligence (MBI) the required privileges to pull data from a third-party service. Re-authorization is required when these privileges are revoked.

## Database and SaaS integrations

For lists of Database and SaaS integrations, refer to [Connecting External Data Using an Integration](https://docs.magento.com/mbi/data-analyst/importing-data/integrations/integrations.html) in our developer documentation. (When opening the page, use the table of contents on the left for navigation).

## Having connection issues?

Authorizing an integration grants MBI the required privileges to pull data from a third party service. Re-authorization is required when these privileges are revoked.

This could happen due to a number of reasons:

* an issue with the third party service
* authentication token expiration
* a change made on your administrative account
* or an internal issue within MBI

The status of all integrations is on the Integrations page ( **Manage Data > Integrations** ):

![Integrations_page.png](assets/Integrations_page.png)

To re-authenticate, you may have to re-enter your account credentials. In some cases, you may be required to generate new API keys for the problem integration. Click the name of the problem integration to begin the re-authorization process.

If the problem persists, please [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).
