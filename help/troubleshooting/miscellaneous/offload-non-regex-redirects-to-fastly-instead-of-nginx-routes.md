---
title: 'Offload non-[!DNL regex] redirects to [!DNL Fastly] instead of [!DNL Nginx] (routes)'
description: This topic suggests a solution to a typical redirects performance issue you might have when you offload non-[!DNL regex] redirects to [!DNL Fastly] instead of [!DNL Nginx] in Adobe Commerce on cloud infrastructure.
exl-id: 8b22d25d-0865-4d21-b275-d344ba8748f2
feature: Routes
role: Developer
---
# Offload non-[!DNL regex] redirects to [!DNL Fastly] instead of [!DNL Nginx] (routes)

This topic suggests a solution to a typical redirects performance issue you might have when you offload non-[!DNL regex] redirects to [!DNL Fastly] instead of [!DNL Nginx] in Adobe Commerce on cloud infrastructure.

## Affected products and versions

* Adobe Commerce on cloud infrastructure (all versions) `Master/Production/Staging` environments leveraging [!DNL Fastly]

## Issue

In Adobe Commerce on cloud infrastructure, large numbers of non-[!DNL regex] redirects/rewrites can't be done at the [!DNL Nginx] layer, and as a result, can cause performance issues.

## Cause

The `routes.yaml` file in the `.magento/routes.yaml` directory defines routes for your Adobe Commerce on cloud infrastructure.

If the size of your `routes.yaml` file is 32KB or larger, you should offload your non-[!DNL regex] redirects/rewrites to [!DNL Fastly].

This [!DNL Nginx] layer can't handle a large number of non-[!DNL regex] redirects/rewrites, or performance issues will result.

## Solution

The solution is to offload those non-[!DNL regex] redirects to [!DNL Fastly] instead. Create a generic error path to redirect to [!DNL Fastly].

The following steps will detail how to place redirects on [!DNL Fastly] instead of [!DNL Nginx].

1. Create an Edge Dictionary.

   First, you can use [[!DNL VCL] snippets in Adobe Commerce](/docs/commerce-cloud-service/user-guide/cdn/custom-vcl-snippets/fastly-vcl-custom-snippets.html) to define an edge dictionary. This will contain the redirects.

   Some caveats to this:

   * [!DNL Fastly] can't do [!DNL regex] on dictionary entries. It's only an exact match. For more on these limitations, please see [[!DNL Fastly]'s docs on edge dictionary limitations](https://docs.fastly.com/guides/edge-dictionaries/about-edge-dictionaries#limitations-and-considerations).
   * [!DNL Fastly] has a limit of 1000 entries into a single dictionary. [!DNL Fastly] can expand this limit, but that leads to the third caveat.
   * Any time you update the entries and deploy that updated [!DNL VCL] to all the nodes, there is a geometric load time increase with expanding dictionaries - meaning, a 2000-entry dictionary will actually load 3x-4x slower than a 1000-entry dictionary. But that is only an issue when you're deploying the [!DNL VCL] (updating the dictionary or changing the [!DNL VCL] function code).

     It does not impact the time it takes [!DNL Fastly] to process a request; it just impacts how long it takes [!DNL Fastly] to push out a new configuration.

     Generally speaking, configuration changes take a few seconds on average, usually no more than 5-10 seconds. So a 2x increase in dictionary items takes upwards of 30 seconds to get your config rolled out. A 4x increase would take closer to 2 minutes. This leads to the fourth caveat.

   * There is a pretty hard limit of 10,000 entries into an edge dictionary.

   It is strongly recommended to consolidate down your redirects list. You can use multiple dictionaries, but please just be aware that any update you make to your [!DNL VCL] will take several minutes to actually populate across [!DNL Fastly].

1. Compare the [!DNL URL] to the Dictionary(ies).

   When the [!DNL URL] lookup occurs, this will make the comparison to apply the custom error code if a match is found.

   Use another [!DNL VCL] snippet to add something like the following to `vcl_recv`:

   ```
        declare local var.redir-path STRING;
        set var.redir-path = table.lookup(redirects, std.tolower(req.url), "");

        if (var.redir-path != "") {
          error 912 var.redir-path;
        }
   ```

   Here, we're checking to see if the [!DNL URL] exists in the table entry. If it does, we're calling an internal [!DNL Fastly] error and passing into that error the redirect [!DNL URL] from the table.

1. Manage the Redirect.

   When a match is found, the action is taken that is defined for that `obj.status`, in this case a 301 permanent move redirect.

   Use a final snippet in `vcl_error` to send the 301 error codes back to the client:

   ```
     if (obj.status == 912) {
        set obj.http.location = obj.response;
        set obj.status = 301;
        set obj.response = "Moved Permanently";
        return(deliver);
          }
   ```

   With this block, we're checking to see if the error code passed in from `vcl_recv` matches, and if so, we'll set the location to the error message passed in, then change the status code to 301 and the message to "Moved Permanently". At that point, the response should be ready to go back to the client.

### Stage Service

>[!WARNING]
>
>If you would like to try all of these steps out, it is strongly recommended to set up an Adobe Commerce staging environment. That way, you can run tests against the [!DNL Fastly] service to make sure everything behaves as you would expect.

If you don't want to run an Adobe Commerce staging environment, but you would like to see how these redirects would look, you can set up a stage account directly on [!DNL Fastly].

## Related reading

* [[!DNL Fastly VCL] reference](https://docs.fastly.com/vcl/)
* [Configure routes](/docs/commerce-cloud-service/user-guide/configure/routes/routes-yaml.html) in our developer documentation
* [Set up [!DNL Fastly]](/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration.html) in our developer documentation
* [[!DNL VCL] regular expression cheat sheet](https://docs.fastly.com/en/guides/vcl-regular-expression-cheat-sheet) in our developer documentation
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
