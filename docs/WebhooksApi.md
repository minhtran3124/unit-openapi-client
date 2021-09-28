# openapi_client.WebhooksApi

All URIs are relative to *http://example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dispatch_event**](WebhooksApi.md#dispatch_event) | **POST** /webhooks/events/78 | Dispatch Event


# **dispatch_event**
> dispatch_event(content_type, body)

Dispatch Event

Remove 'balance' and 'hold' from the request

### Example

* Bearer Authentication (bearer):
```python
import time
import openapi_client
from openapi_client.api import webhooks_api
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_api.WebhooksApi(api_client)
    content_type = "application/vnd.api+json" # str | 
    body = "{}" # str | Remove 'balance' and 'hold' from the request

    # example passing only required values which don't have defaults set
    try:
        # Dispatch Event
        api_instance.dispatch_event(content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling WebhooksApi->dispatch_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  |
 **body** | **str**| Remove &#39;balance&#39; and &#39;hold&#39; from the request |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

