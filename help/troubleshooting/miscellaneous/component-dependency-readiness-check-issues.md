---
title: Component dependency readiness check issues
description: This article provides solutions for component dependency conflicts.
exl-id: e0865226-2aaf-4bdd-8c28-28f32f38ce0c
feature: Configuration
role: Developer
---
# Component dependency readiness check issues

This article provides solutions for component dependency conflicts.

## Resolve component dependency conflicts {#resolve-component-dependency-conflicts}

We suggest you try the following solutions in the order shown:

1. [Conflicting dependencies](#trouble-depend-conflict)
1. [File system permissions issues](#trouble-depend-permission)
1. [The Component Dependency Check status never changes](#trouble-depend-state)

### Conflicting dependencies {#trouble-depend-conflict}

The message *We found conflicting component dependencies* displays if Composer cannot determine which components to install or update. To resolve component dependency issues, you should be a technical person who thoroughly understands how Composer works.

Following is a sample failure message:

```bash
We found conflicting component dependencies.
 You are trying to update package(s) magento/module-sample-data to 1.0.0-beta
 We've detected conflicts with the following packages:
 - magento/sample-data version 0.74.0-beta15. Please try to update it to one of the following package versions: 0.74.0-beta16, 0.74.0-beta14, 0.74.0-beta13, 0.74.0-beta12, 0.74.0-beta11, 0.74.0-beta10, 0.74.0-beta9, 0.74.0-beta8, 0.74.0-beta7
```

>[!NOTE]
>
>The message you see will likely be different.

Refer to [Conflicting component dependencies for a solution](/help/troubleshooting/miscellaneous/conflicting-component-dependencies.md) in our support knowledge base.

## File system permissions issues {#trouble-depend-permission}

If the Adobe Commerce file system owner doesn't have the permissions to write to directories on the Adobe Commerce file system, a message similar to the following displays:

```bash
file_put_contents(/var/www/html/magento2/var/composer_home/cache/repo/https---
packagist.org/provider-doctrine$instantiator.json): failed to open stream: Permission denied
```

Make sure you set file system permissions as discussed in the article [Overview of ownership and permissions](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/file-system/overview) in our developer documentation.

## The Component Dependency Check status never changes {#trouble-depend-state}

In some cases, the status of the Component Dependency Check doesn't change, even after you try to correct issues. In that case, you can either delete or rename files named `<magento_root>/var/.update_cronjob_status` and `<magento_root>/var/.setup_cronjob_status` and try running the Component Manager again.

Renaming or removing these files forces the Component Manager to run the checks again.
