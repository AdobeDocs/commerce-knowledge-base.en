---
title: Safely delete files when disk run out of space in Adobe Commerce on cloud infrastructure
description: This article provides a solution for when you run out of disk space and need to safely remove files. Before considering this action, review [Manage disk space](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space#no-space-left) in our developer documentation. If the steps in that article are not appropriate for you or do not solve the issue, review the steps in this article.
exl-id: 6b0a5c1a-8db4-49d7-a785-b4e0bbaea0df
feature: Cloud, Paas
role: Developer
---
# Safely delete files when disk run out of space in Adobe Commerce on cloud infrastructure

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.4.2 - 2.4.7
* This is specific to dedicated Pro clusters. Starter and Integration environments are single node, and do not have the `/data/exports` directory.

## Signs of low disk space

Signs you are running out of disk space can be stuck deployment, disk full warnings, and poor performance.
To see the amount of disk space used by the file system run the following command in the CLI/Terminal:

`df -h`


## How to safely delete files to increase disk space

You can delete files from the application's mount points, from your `/app` path or through `/mnt/shared`. They are two different ways to access the same files.

>[!WARNING]
>
>**Never modify or delete the contents of `/data/exports`**.
>
>`/data/exports` is the underlying storage behind the shared filesystem, and it is managed by GlusterFS.
>
>The filesystem there contains not only the file contents, but metadata about the state of the filesystem to allow for synchronization >between the nodes of your cluster. **Changing or deleting files directly within this filesystem will corrupt the shared >filesystem, requiring extensive repairs or data recovery.**

To locate the largest files that might be good candidates for clearing, run the following command (on large or busy projects can take up to an hour):

```bash
FS='/data/exports';NUMRESULTS=20;resize;clear; echo "Please find below the Largest Directories and Files:";date;df -h $FS; echo "Largest Directories:";nice -n 19 find /app/*/ -type d -ls 2>/dev/null| sort -rnk1| head -n $NUMRESULTS| awk '
{printf "%d MB %s\n", $1/1024,$2}
';echo "Largest Files:"; nice -n 19 find /app/*/ -type f -ls 2>/dev/null| sort -rnk7| head -n $NUMRESULTS|awk '
{printf "%d MB\t%s\n", ($7/1024)/1024,$NF}
'; echo "Please use the above information to clear any unwanted data from the server, it is important this is done as soon as possible to ensure your server stays functional.";
```

The output of the command will contain a list of the largest files and directories with their sizes specified.

## Related reading

In our support knowledge base:

* [Increase disk space for Integration environment on Cloud](/help/how-to/general/increase-disk-space-for-integration-environment-on-cloud.md)
* [Low disk space](/help/troubleshooting/miscellaneous/low-disk-space.md)

In our developer documentation:

* [Manage disk space](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space)
