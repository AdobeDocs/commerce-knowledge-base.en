---
title: Composer install command overides .gitignore file, Adobe Commerce
description: This article provides a solution for when a tracked `.gitignore` file is overriden by composer on Adobe Commerce on cloud infrastructure 2.4.2-p1 and 2.3.7.
exl-id: b0604bae-d630-4292-88d7-6945db30fcf4
feature: Install, Upgrade
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 6388cf7b-8a81-5248-a1e4-7bb57bbe250f
    internal-label: Install
  - id: a8ae7a5a-6cdc-5922-bd0d-6feb44b04984
    internal-label: Upgrade
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Composer install command overides .gitignore file, Adobe Commerce

This article provides a solution for when a tracked `.gitignore` file is overriden by composer on Adobe Commerce on cloud infrastructure 2.4.2-p1 and 2.3.7.

## Affected products and versions

Adobe Commerce on cloud infrastructure 2.4.2-p1 and 2.3.7.

## Issue

`.gitignore` file is being overwritten when running composer install command.

<u>Steps to reproduce</u>:


1. Create an empty directory for your workspace.
1. Run this command in the root directory:

    ```bash
    composer create-project --repository-url=https://repo.magento.com/ magento/project-community-edition:2.4.2-p1.
    ```
    
    \# or 2.3.7

1. Then run the following commands:
    1. `echo "/this/line/should/stay" >> .gitignore`
    1. `git init`
    1. `git add * && git add .*`
    1. `git commit -m "Init"` # file commited to repo
    1. `rm -rf vendor/*`
    1. `composer install`
    1. `git diff`

        ```git
        diff --git a/.gitignore b/.gitignore
        index c144521..7092a56 100644
        --- a/.gitignore
        +++ b/.gitignore
        @@ -70,4 +70,3 @@ atlassian*
        /generated/*
        !/generated/.htaccess
        .DS_Store
        -/this/line/should/stay
        ```

<u>Expected result</u>:

`.gitignore` is not overriden by composer.

<u>Actual result</u>:

`.gitignore` is overriden by every composer install run.

## Solution

To keep your custom `.gitignore file` you need to ignore it in the `magento-deploy-ignore` section.

```git
{
...
"extra": {
    "magento-deploy-ignore": {
        "*": [
            "/.gitignore"
        ]
    }
    ...
}
```


## Related reading

* [Tracked .gitignore file is overriden by composer!](https://github.com/magento/magento2/issues/32888) in Magento2 GitHub.
