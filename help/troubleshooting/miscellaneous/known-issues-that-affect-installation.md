---
title: Known issues that affect xdebug installation
description: This article provides a solution for when you experience an exception error when you use the optional PHP extension `xdebug`.
exl-id: 5090ea99-e0c3-436a-809b-109701740927
feature: Install
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 6388cf7b-8a81-5248-a1e4-7bb57bbe250f
    internal-label: Install
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Known issues that affect xdebug installation

This article provides a solution for when you experience an exception error when you use the optional PHP extension `xdebug`.

* During installation
* Accessing either the Commerce Admin or storefront after a successful installation

Sample exception:

```php
Fatal error: Maximum function nesting level of '100' reached, aborting!
```

To resolve this issue, you can:

* Disable the `xdebug` extension.
* Set the value of `xdebug.max_nesting_level` to a value of 200 or more. For more information, see [xdebug documentation](http://xdebug.org/docs/basic#max_nesting_level).

After you change the configuration of or disable `xdebug`, restart Apache:

* CentOS: `sudo service httpd restart`
* Ubuntu: `sudo service apache2 restart`
