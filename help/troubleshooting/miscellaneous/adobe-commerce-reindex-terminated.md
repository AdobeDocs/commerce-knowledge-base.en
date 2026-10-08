---
title: 'Adobe Commerce cloud: reindex is terminated with `Killed` message'
description: '* Adobe Commerce on cloud infrastructure (all versions)'
exl-id: 36ed9c9f-8280-41db-9df3-fe842dade4b1
feature: Cloud, Paas
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 5a951749-fac9-5bc7-9a98-ebe4ff066437
    internal-label: Cloud
  - id: 00451af3-7b97-5414-9992-3a6c269e413f
    internal-label: Paas
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce cloud: reindex is terminated with `Killed` message

## Affected products and versions

* Adobe Commerce on cloud infrastructure (all versions)

## Issue

You are trying to run a reindex on the Integration branch (or on Staging of the Starter architecture project), and the process is being terminated with the `Killed` message.

## Cause

This usually happens because the PHP processes are running out of memory.
The most common reason for that is a large number of products, stores, and/or customer groups on the instance.

## Solution

1. Reduce the number of products (as well as customer groups and stores - if applicable).
1. Limit use to one or two concurrent users.
1. Disable cron jobs, and run manually as needed.
1. If this has not been done previously, request an upgrade to the Enhanced Integration environments - take note of the restriction on the number of environments you would be limited to once the upgrade has been performed. Refer to the [Integration Environment enhancement request - Pro and Starter](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27242) article in our support knowledge base for details.

## Related reading:

In our developer documentation:

* [Pro architecture > Integration environment](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/pro-architecture#integration-environment)
* [Starter architecture > Staging environment](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/starter-architecture#cloud-arch-stage)
