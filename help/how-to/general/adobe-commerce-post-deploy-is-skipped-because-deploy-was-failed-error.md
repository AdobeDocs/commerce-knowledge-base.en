---
title: Adobe Commerce post-deploy is skipped because deploy was failed error
description: "This article explains how to investigate a deployment error: *Post-deploy is skipped because deploy was failed* error"
---

# Adobe Commerce post-deploy is skipped because deploy was failed error

This article explains how to investigate a deployment error: *Post-deploy is skipped because deploy was failed* which occurs during deployment to different environments, for example upgrading.

## Affected products and versions

Adobe Commerce on cloud infrastructure [all supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## Issue

The deployment fails and returns a generic error message, so it's not clear on how to resolve the error.

## Cause

Undetermined - what causes this error message depends on the code and database that is deployed.

## How to investigate the deployment error 

```
[20XX-XX-XX XX:XX:XX] DEBUG: Running step: is-deploy-failed
    W:
    W: In Processor.php line 129:
    W:
    [20XX-XX-XX XX:XX:XX] ERROR: [201] Post-deploy is skipped because deploy was failed.
    W:   Post-deploy is skipped because deploy was failed.
    W:
    W:
    W: In DeployFailed.php line 39:
    W:
    W:   Post-deploy is skipped because deploy was failed.
    W:
    W:
    W: post-deploy
    W:
```

To obtain the error trace for determining the actual cause, SSH to the server and check the log file *var/log/install_upgrade.log*
