

from __future__ import absolute_import

import re  # noqa: F401


import six
import json
import uuid
from Veem.VeemError import VeemError
from Veem.models.invoice_response import InvoiceResponse
from Veem.api_client import ApiClient
import requests
from Veem.configuration import Configuration



class InvoiceControllerApi(object):


    def __init__(self,  access_token,api_client=None,):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.config=Configuration()
        self.invoice_url=self.config.host+"invoices"
        self.access_token=access_token



    def deserialize(self,response):
            requestId=response['requestId']
            amount=response['amount']
            number=amount['number']
            currency=amount['currency']

            try:
                payer=response['payer']
                email=payer['email']
                countryCode=payer['countryCode']
                phone=payer['phone']
            except KeyError as k:
                email=None
                countryCode=None
                phone=None

            id=response['id']
            status=response['status']

            exchangeRate=response['exchangeRate']
            fromAmount=exchangeRate['fromAmount']
            toAmount=exchangeRate['toAmount']
            fromCurrency=exchangeRate['fromCurrency']
            toCurrency=exchangeRate['toCurrency']

            try:
                claimLink=response['claimLink']
            except KeyError as k:
                claimLink=None

            responseObject=InvoiceResponse(request_id=requestId, amount_number=number, amount_currency=currency,payer_email=email, payer_country_code=countryCode, payer_phone=phone, status=status, id=id, exchange_rate_from_amount=fromAmount,exchange_rate_to_amount=toAmount,exchange_rate_from_currency=fromCurrency, exchange_rate_to_currency=toCurrency,claim_link=claimLink)
            return responseObject


    def approve_invoice_using_post(self, invoice_id, **kwargs):  # noqa: E501
        """approveInvoice  # noqa: E501

        approve an invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.approve_invoice_using_post(invoice_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int invoice_id: invoiceId (required)
        :return: InvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.approve_invoice_using_post_with_http_info(invoice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.approve_invoice_using_post_with_http_info(invoice_id, **kwargs)  # noqa: E501
            return data

    def approve_invoice_using_post_with_http_info(self, invoice_id, **kwargs):  # noqa: E501
        """approveInvoice  # noqa: E501

        approve an invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.approve_invoice_using_post_with_http_info(invoice_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int invoice_id: invoiceId (required)
        :return: InvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method approve_invoice_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_id' is set
        if ('invoice_id' not in params or
                params['invoice_id'] is None):
            raise ValueError("Missing the required parameter `invoice_id` when calling `approve_invoice_using_post`")  # noqa: E501

        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url = self.invoice_url+"/"+str(invoice_id)+"/approve"
        response = requests.request("POST", url,headers=header_params)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err


    def cancel_invoice_using_post(self, invoice_id, **kwargs):  # noqa: E501
        """cancelInvoice  # noqa: E501

        cancel an invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.cancel_invoice_using_post(invoice_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int invoice_id: invoiceId (required)
        :return: InvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.cancel_invoice_using_post_with_http_info(invoice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_invoice_using_post_with_http_info(invoice_id, **kwargs)  # noqa: E501
            return data

    def cancel_invoice_using_post_with_http_info(self, invoice_id, **kwargs):  # noqa: E501
        """cancelInvoice  # noqa: E501

        cancel an invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.cancel_invoice_using_post_with_http_info(invoice_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int invoice_id: invoiceId (required)
        :return: InvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_invoice_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_id' is set
        if ('invoice_id' not in params or
                params['invoice_id'] is None):
            raise ValueError("Missing the required parameter `invoice_id` when calling `cancel_invoice_using_post`")  # noqa: E501

        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url = self.invoice_url+"/"+str(invoice_id)+"/cancel"
        response = requests.request("POST", url,headers=header_params)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err

    def create_invoice_using_post(self, request, **kwargs):  # noqa: E501
        """createInvoice  # noqa: E501

        posts an invoice and sends to receiver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_invoice_using_post(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param InvoiceRequest request: request (required)
        :return: InvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_invoice_using_post_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_invoice_using_post_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def create_invoice_using_post_with_http_info(self, request, **kwargs):  # noqa: E501
        """createInvoice  # noqa: E501

        posts an invoice and sends to receiver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_invoice_using_post_with_http_info(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param InvoiceRequest request: request (required)
        :return: InvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_invoice_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_invoice_using_post`")  # noqa: E501
        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url = self.invoice_url
        response = requests.request("POST", url,headers=header_params,data=json.dumps(request.to_dict()))
        if(response.status_code==201):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err

    def get_invoice_using_get(self, invoice_id, **kwargs):  # noqa: E501
        """getInvoice  # noqa: E501

        get invoice details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_invoice_using_get(invoice_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int invoice_id: invoiceId (required)
        :return: InvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_invoice_using_get_with_http_info(invoice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_invoice_using_get_with_http_info(invoice_id, **kwargs)  # noqa: E501
            return data

    def get_invoice_using_get_with_http_info(self, invoice_id, **kwargs):  # noqa: E501
        """getInvoice  # noqa: E501

        get invoice details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_invoice_using_get_with_http_info(invoice_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int invoice_id: invoiceId (required)
        :return: InvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_invoice_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_id' is set
        if ('invoice_id' not in params or
                params['invoice_id'] is None):
            raise ValueError("Missing the required parameter `invoice_id` when calling `get_invoice_using_get`")  # noqa: E501

        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url = self.invoice_url+"/"+str(invoice_id)
        response = requests.request("GET", url,headers=header_params)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err
