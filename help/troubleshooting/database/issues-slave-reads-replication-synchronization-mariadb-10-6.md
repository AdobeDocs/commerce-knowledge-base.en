---
title: Issues with Slave Reads and Replication Synchronization with MariaDB 10.6
description: This article talks about troubleshooting issues with Slave Reads and Replication Synchronization with MariaDB 10.6.
feature: Configuration
role: Developer
---
# Issues with Slave Reads and Replication

This article provides a solution for unexpected behavior when using Read Replicas on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6+. This includes replication delays, indexer having the incorrect status, and `synchronous_replication` is defaulting to *true* in ece-tools.

## Affected products and versions

* MariaDB 10.6+
* Adobe Commerce on cloud infrastructure 2.4.6

## Issue

You are experiencing replication delays on Adobe Commerce 2.4.6 and MariaDB 10.6.

## Cause

 Adobe Commerce replication configuration does not match the database cluster synchronous replication configuration. 

## Solution

The `slave_parallel_mode` parameter should be set to *conservative*. [Raise a support ticket](/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html?lang=en#submit-ticket) if this is not the case.

Update .magento.env.yaml to:

```yaml
DATABASE_CONFIGURATION:
    _merge: true
        slave_connection:
            default:
                synchronous_replication: false
```

## Related reading

* [Configure environment variables for deployment](docs/commerce-cloud-service/user-guide/configure/env/configure-env-yaml.html)
* [Best practices for database configuration](docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html)
