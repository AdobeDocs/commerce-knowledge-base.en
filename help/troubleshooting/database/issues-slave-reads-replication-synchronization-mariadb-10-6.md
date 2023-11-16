---
title: Issues with Slave Reads and Replication Synchronization with MariaDB 10.6
description: This article talks about troubleshooting issues with Slave Reads and Replication Synchronization with MariaDB 10.6.
feature: Configuration
role: Developer
---
# Issues with Slave Reads and Replication

This article provides a solution for unexpected behavior when using Read Replicas on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6+. 

## Affected products and versions

* MariaDB 10.6+
* Adobe Commerce on cloud infrastructure 2.4.6

## Issue

Non critical reads are showing incorrect information. 

## Cause

The `slave_parallel_mode` config on the database was changed by default to *optimistics*, the incorrect value (should be *conservative*, and the `synchronous_replication` value in ece-tools is defaulting to *true* (should be *false*).

## Solution

The `slave_parallel_mode` parameter should be set to *conservative*. To check run the following command:

```
MariaDB [main]> show variables like 'slave_parallel_mode';
+---------------------+--------------+
| Variable_name       | Value        |
+---------------------+--------------+
| slave_parallel_mode | conservative |
+---------------------+--------------+
1 row in set (0.001 sec)
```

[Raise a support ticket](/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html?lang=en#submit-ticket) if this is not the case.

Update .magento.env.yaml to:

```yaml
DATABASE_CONFIGURATION:
    _merge: true
        slave_connection:
            default:
                synchronous_replication: false
```

## Related reading

* [Configure environment variables for deployment](/docs/commerce-cloud-service/user-guide/configure/env/configure-env-yaml.html)
* [Best practices for database configuration](/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html)
