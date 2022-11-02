---
title: Error purging cache in Commerce Admin
description: "This article explains how to identify the cause of an error message that occurs when purging the cache in the Commerce Admin. When you attempt to purge cache through the Admin, you receive the following message:"
---

# Error purging cache in Commerce Admin

This article explains how to identify the cause of an error message that occurs when purging the cache in the Commerce Admin. When you attempt to purge cache through the Admin, you receive the following message:
*/app/project-id/pub/media/catalog/product/cache/directory/filename" file can't be deleted. Warning!unlink(/app/project id/pub/media/catalog/product/cache/directory/filename): No such file or directory*

## Affected products and versions

Adobe Commerce (all deployment methods) 2.3.0-2.3.7, 2.4.0-2.4.2-p1

## Issue

When you attempt to purge cache through the Admin, you receive an error message.

<u>Steps to reproduce:</u>

1. In the Admin, go to **System** > **Tools** > **Cache Management**.
1. Select any of the clear caching options.

<u>Expected result:</u>

You successfully flush Adobe Commerce cache with no errors.

<u>Actual result:</u>

You get the "file cannot be deleted" error.

## Cause

The error is related to a delay between the time that the cache cleaning operation was initiated and when it was reported as completed.

## Solution

1. Confirm that the files mentioned in the error are not present on the server (checking that the cache purge was successful):

```bash
ls -la pub/media/catalog/product/cache/directory/filename
```

If you see the following output:

```bash
ls: cannot access 'pub/media/catalog/product/cache/directory/filename/': No such file or directory
```

there was an attempt to clear the files when the operation had already been completed. This is not a bug; it is a messaging concurrency issue that is expected to happen sometimes. There is no issue to troubleshoot.
However, if the output shows that the files are still in the cache, you need to [submit a support ticket](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html#submit-ticket).

## Related Reading

* [Cache Management](https://docs.magento.com/user-guide/system/cache-management.html) in our developer documentation.