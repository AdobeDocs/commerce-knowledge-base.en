---
title: Read Replicas issues on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6
description: This article explains how to troubleshoot Read Replicas issues on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6.
feature: Configuration
role: Developer, Admin
---

# Read Replicas issues on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6

This article provides solutions for unexpected behavior when using Read Replicas on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6+. 

## Affected products and versions

* MariaDB 10.6+
* Adobe Commerce on cloud infrastructure 2.4.6

## Issue

Non-critical reads are showing incorrect information. 

## Cause

The `slave_parallel_mode` config on the database was changed by default to *optimistics* when the value should be *conservative*, and the `synchronous_replication` value in Ece-Tools is defaulting to *true* when the value should be *false*.

## Solution

1. Check that the `slave_parallel_mode` parameter is set to *conservative*. To do so run the following command:

```
MariaDB [main]> show variables like 'slave_parallel_mode';
+---------------------+--------------+
| Variable_name       | Value        |
+---------------------+--------------+
| slave_parallel_mode | conservative |
+---------------------+--------------+
1 row in set (0.001 sec)
```

[Raise a support ticket](/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html?lang=en#submit-ticket) if the value is not showing as *conservative*.

1. Update `.magento.env.yaml` database configurations to:

```yaml
DATABASE_CONFIGURATION:
    _merge: true
        slave_connection:
            default:
                synchronous_replication: false
```

For steps on updating the database configuration, refer to [DATABASE_CONFIGURATION](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-deploy.html#database_configuration) in Deploy variables > in the Commerce on Cloud Infrastructure Guide. 


## Related reading

* [Configure environment variables for deployment](/docs/commerce-cloud-service/user-guide/configure/env/configure-env-yaml.html) in the Commerce on Cloud Infrastructure Guide.
* [Best practices for database configuration](/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html) in the Implementation Playbook.
