---
title: 'Email stating that the exports storage is almost full'
description: This article provides a solution for the issue where you receive an email stating that the exports storage is almost full.
feature: Cloud, Storage, Media
role: Developer
---
# Email stating that exports storage is almost full

This article provides a solution for the issue where you receive an email stating that the exports storage is almost full.

## Affected products and versions

Adobe Commerce on cloud infrastructure (all versions)

## Issue

You receive an email with the following content but are unable to locate the *exports* folder:

*Our monitoring has detected that the 'exports' storage on your cluster XXX is around '85%' full.*
*If needed, please review the usage, do a clean up, or request for an upsize.*
*Also, note that we will attempt an upsize automatically when storage reaches the critical-threshold level.*

## Cause

The email is referring to the **exports** storage, which is the amount of disk allocated to the files/media, and not a specific folder named *exports*.

## Solution

You should review the files usage in the environment. Run this command to obtain the existing usage:

`df -h |grep data`

The typical locations where the files storage is likely to be filled up are the *pub/media/catalog/product/cache* or *var/log* folders. To determine the disk space used by the files, run this command with the appropriate path */path/to/folder*:

`du -shc` */path/to/folder*

If the media disk usage constitutes a large proportion of the total disk space, you may want to consider enabling [Fastly Deep Image Optimization](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/fastly-image-optimization#deep-image-optimization), and then delete the files in the *pub/media/catalog/product/cache* folder on the server manually.

## Related Reading

[Check dedicated clusters](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space#check-dedicated-clusters) in our support knowledge base.