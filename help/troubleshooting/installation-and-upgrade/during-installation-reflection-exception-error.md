---
title: During installation, Reflection Exception error
description: This article provides a solution for the Reflection Exception error during installation.
exl-id: aed5f297-1339-4171-9392-04b3f93277ee
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
# During installation, Reflection Exception error

This article provides a solution for the Reflection Exception error during installation.

## Details {#details}

During the installation, a message similar to the following displays:

```php
[ERROR] exception 'ReflectionException' with message 'Class Magento\Framework\StoreManagerInterface does not exist' in /<path>/lib/internal/Magento/Framework/Code/Reader/ClassReader.php
```

## Solution {#solution}

Clear all directories and files under Adobe Commerce's `var` subdirectory and install the Adobe Commerce software again.

As the [Adobe Commerce file system owner](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/file-system/overview) or as a user with `root` privileges, enter the following commands:

```bash
$ cd <your Magento install directory>/var
```

```bash
$ rm -rf var/cache/* di/* generation/* page_cache/*
```

### Redis {#redis}

If you use Redis and still get an error, clear the Redis cache as follows:

```bash
$ redis-cli FLUSHALL
```
