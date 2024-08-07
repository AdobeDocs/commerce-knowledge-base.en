---
title: '[!DNL B2B] 1.4.0 installation fails on Adobe Commerce 2.4.6-p1 on-premises'
description: This article provides a workaround for the Adobe Commerce 2.4.6-p1 on-premises issue where [!DNL B2B] version 1.4.0 installation fails.
feature: Install, Upgrade, B2B
role: Developer
exl-id: 4a557c13-7ec2-4cfe-b86e-bb0d1a441658
---
# [!DNL B2B] 1.4.0 installation fails on Adobe Commerce 2.4.6-p1 on-premises

This article provides a workaround for the Adobe Commerce 2.4.6-p1 on-premises issue where [!DNL B2B] version 1.4.0 installation fails.

## Affected products and versions

* Adobe Commerce 2.4.6-p1 **on-premises**
* [!DNL B2B] version 1.4.0

>[!NOTE]
>
>[!DNL B2B] version 1.4.0 successfully installs on **Adobe Commerce Cloud 2.4.6-p1**.

## Issue

 <u>Steps to reproduce</u>:

1. Install Adobe Commerce 2.4.6-p1.

    ```bash
    m2install.sh -s composer --ee -v 2.4.6-p1
    ```

1. Try to install [!DNL B2B] version 1.4.0.

    ```bash
    composer require magento/extension-b2b:1.4.0
    ```

<u>Expected results</u>:

[!DNL B2B] version 1.4.0 installs on Adobe Commerce 2.4.6-p1 successfully.

<u>Actual results</u>:

Installation fails with the below error:

```bash
Your requirements could not be resolved to an installable set of packages.

  Problem 1
    - Root composer.json requires magento/extension-b2b 1.4.0 -> satisfiable by magento/extension-b2b[1.4.0].
    - magento/extension-b2b 1.4.0 requires magento/security-package-b2b 1.0.4-beta1 -> found magento/security-package-b2b[1.0.4-beta1] but it does not match your minimum-stability.


Installation failed, reverting ./composer.json and ./composer.lock to their original content.
```

## Workaround

Successfully install or upgrade to [!DNL B2B] version 1.4.0 on Adobe Commerce 2.4.6-p1 by adding manual dependencies for the [!DNL B2B] security package with a [stability tag](https://getcomposer.org/doc/04-schema.md#package-links).

1. From the Adobe Commerce installation directory, update `composer.json` with the required dependencies:

   ```bash
   composer require magento/module-re-captcha-company=1.0.3-beta1@beta magento/security-package-b2b=1.0.4-beta1@beta
   ```

   **Command output:**

   ```bash
   Running composer update magento/module-re-captcha-company magento/security-package-b2b
   Loading composer repositories with package information
   Updating dependencies
   Lock file operations: 2 installs, 0 updates, 0 removals
     - Locking magento/module-re-captcha-company (1.0.3-beta1)
     - Locking magento/security-package-b2b (1.0.4-beta1)
   Writing lock file
   Installing dependencies from lock file (including require-dev)
   Package operations: 2 installs, 0 updates, 0 removals
     - Downloading magento/module-re-captcha-company (1.0.3-beta1)
     - Installing magento/module-re-captcha-company (1.0.3-beta1): Extracting archive
     - Installing magento/security-package-b2b (1.0.4-beta1)
   1 package suggestions were added by new dependencies, use `composer suggest` to see details.
   Package sebastian/phpcpd is abandoned, you should avoid using it. No replacement was suggested.
   Generating autoload files
   132 packages you are using are looking for funding.
   Use the `composer fund` command to find out more!
   No security vulnerability advisories found
   ```

1. Update `composer.json` to add [!DNL B2B] version 1.4.0.

   ```bash
   composer require magento/extension-b2b=1.4.0
   ```

   **Command output:**

   ```bash
   ./composer.json has been updated
   Running composer update magento/extension-b2b
   Loading composer repositories with package information
   Updating dependencies
   ...
   Generating autoload files
   132 packages you are using are looking for funding.
   Use the `composer fund` command to find out more!
   No security vulnerability advisories found
   ```

1. Complete the installation or upgrade process.

   * [Install [!DNL B2B] on cloud infrastructure](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure-store/b2b-module.html)
   * [Install on-premises](https://experienceleague.adobe.com/docs/commerce-admin/b2b/install.html)
