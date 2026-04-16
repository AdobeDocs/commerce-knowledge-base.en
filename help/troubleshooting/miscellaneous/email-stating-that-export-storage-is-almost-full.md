---
title: Email stating that the exports storage is almost full
description: This article provides a solution for the issue where you receive an email stating that the exports storage is almost full.
feature: Cloud, Storage, Media
role: Developer
exl-id: 7dae295c-919c-46c5-bf63-7d3467c2e07f
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

The alert refers to the exports storage filesystem, which is the disk volume where media and other file data are stored. This filesystem is typically mounted at `/data/exports`. The alert does not indicate the presence of a single directory literally named exports.

To confirm what the alert refers to, check the exports storage usage:

1. Run `Shelldf -h | grep`, and the following example output:

    ```
    /dev/nvme1n1 50G 38G 12G 77% /data/exports
    tmpfs         7.7G 4.0K 7.7G  1% /data/exports/shared
    ```

* In this example, `/data/exports` is the main exports filesystem:

    * 50 GB total
    * 38 GB used
    * 12 GB available (77% utilization)

* `/data/exports/shared` is a `tmpfs` (in-memory) mount used for shared data and does not contribute significantly to disk pressure.

This confirms that the alert is triggered by the overall disk utilization of `/data/exports`, not by a single folder named exports.

If `/data/exports` shows high utilization, large directories under this filesystem—such as pub/media or other custom file locations—are typically responsible for the increased usage.

## Solution

Follow these steps to review, clean up, and validate exports storage usage.

1. Run the command `df -h | grep exports` to check the current usage of the exports storage filesystem. Review the **Use%** column for `/data/exports`:

    * If usage is 70–85%, start planning cleanup.
    * If usage is greater than 90%, take action immediately to avoid write failures or service impact.

1. Identify directories consuming significant disk space under `/data/exports` by running:

    ```bash

    du -sh /data/exports/* 2>/dev/null

    ```

    Look for large directories such as `pub/media` or custom export folders.

1. Clean up files based on the environment:

    * Remove old or unused export files, logs, or temporary data first.
    * In non-production environments, you can usually remove test media or old artifacts more aggressively.
    * In production environments, coordinate with your team before deleting any media or business-critical files.

1. After the cleanup, run the following command `df -h | grep exports` to confirm that the **Use%** value for `/data/exports` has dropped to a safe operating level.

## Related Reading

[Check dedicated clusters](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space#check-dedicated-clusters) in our support knowledge base.
