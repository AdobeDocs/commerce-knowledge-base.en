---
title: During installation, PHP date warning
description: This article provides a fix for a PHP date warning during installation.
exl-id: f82c77a9-bbcd-4426-96a0-b3f4b704860b
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
# During installation, PHP date warning

This article provides a fix for a PHP date warning during installation.

## Details {#details}

During the installation, the following message displays:

```text
PHP Warning:  date(): It is not safe to rely on the system's timezone settings. [more]
```

### Solution {#solution}

Check the PHP time zone setting carefully. Refer to [Installation Guide > PHP Settings](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/php-settings) in our developer documentation.
