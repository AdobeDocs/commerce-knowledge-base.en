---
title: run `setup:static-content:deploy` deployed_version.txt issue
description: This article provides a fix for `deployed_version.txt` is not writable error when running the `setup:static-content:deploy` command manually.
exl-id: 88d8c126-349f-49cd-8f02-2a32e4994521
feature: Deploy, Page Content, SCD
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: bcd8874c-7b93-5596-bdaa-22660e84df14
    internal-label: Deploy
  - id: 17d326fa-534a-55a5-b46f-8ae1de1e2f75
    internal-label: Page Content
  - id: d05f97c9-0a96-5792-92cf-f66ce7326e3a
    internal-label: SCD
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# run `setup:static-content:deploy` deployed_version.txt issue

This article provides a fix for `deployed_version.txt` is not writable error when running the `setup:static-content:deploy` command manually.

## Issue

If you follow the Adobe Commerce on cloud infrastructure recommendations to use Configuration Management (and move static assets generation to the build stage in order to decrease website downtime during deployment), you may face the following error when running the `setup:static-content:deploy` command manually:

```
{{cloud-project-id}}_stg@i:~$ php bin/magento setup:static-content:deploy
Requested languages: en_US
Requested areas: frontend, adminhtml
Requested themes: Magento/blank, Magento/luma, Aheadworks/marketplace, Magento/backend
[Magento\Framework\Exception\FileSystemException]
The path "deployed_version.txt:///app/{{cloud-project-id}}_stg/pub/static/app/{{cloud-project-id}}_stg/pub/static/" is not writable
```

## Cause

We have optimized the deployment process to decrease downtime and have created symlinks to static assets files instead of copying them. The location where the static assets are stored is read-only, that is why you get the error message above.

We strongly do not recommend to run static content deploy manually because all assets are already generated and there will be no difference between files if you do it manually (the theme files are read-only as well, you cannot change them), so there's no sense in such operation.

## Solution

If you still want to run static content deployment, remove symlinks in the `pub/static` directory and run the `setup:static-content:deploy` command again:

```
find pub/static/ -maxdepth 1 -type l -delete
```
