---
title: Low site and API performance
description: This article provides a patch for the known Adobe Commerce on cloud infrastructure 2.2.1 issue related to having a low site and API performance caused by a long time required to write `debug.log`.
exl-id: b71816cd-f580-4c80-9694-585ed051a56d
feature: REST, Observability
role: Developer
---
# Low site and API performance

This article provides a patch for the known Adobe Commerce on cloud infrastructure 2.2.1 issue related to having a low site and API performance caused by a long time required to write `debug.log`.

## Issue

Site performance is slow. API operations run slowly, for example updating products using the `PUT` method. When you take a closer look at the operations using New Relic, most memory and CPU are consumed by writing to `/var/log/debug.log`.

## Solution

To solve the issue, apply the patch. The patch splits and writes the log, payment, and shipping methods logs to separate files.

## Patch

The patch is attached to this article. To download it, scroll down to the end of the article and click the file name or click the following link:

 [Download MDVA-8371\_EE\_2.2.1\_COMPOSER\_v2.patch](assets/MDVA-8371_EE_2.2.1_COMPOSER_v2.patch.zip)

### Compatible Adobe Commerce versions

The patch was created for:

* Adobe Commerce on cloud infrastructure 2.2.1

The patch is also compatible (but might not solve the issue) with the following Adobe versions and editions:

* Adobe Commerce on cloud infrastructure 2.2.0, 2.2.2, 2.2.3
* Adobe Commerce on-premises 2.2.0, 2.2.2, 2.2.3

## How to apply the patch

See [How to apply a composer patch provided by Adobe Commerce](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in our support knowledge base for instructions.

## Attached Files
