"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from typing import Any, Mapping, Optional, Union, cast
from unkey_py import models, utils
from unkey_py._hooks import HookContext
from unkey_py.types import BaseModel, OptionalNullable, UNSET
from unkey_py.utils import get_security_from_env


class Ratelimit(BaseSDK):
    def set_override(
        self,
        *,
        request: Union[
            models.SetOverrideRequestBody, models.SetOverrideRequestBodyTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SetOverrideResponse:
        r"""
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.SetOverrideRequestBody)
        request = cast(models.SetOverrideRequestBody, request)

        req = self.build_request(
            method="POST",
            path="/v1/ratelimits.setOverride",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.SetOverrideRequestBody
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(50, 1000, 1.5, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="setOverride",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "409",
                "429",
                "4XX",
                "500",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.SetOverrideResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.SetOverrideResponseBody]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrBadRequestData)
            raise models.ErrBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrUnauthorizedData)
            raise models.ErrUnauthorized(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrForbiddenData)
            raise models.ErrForbidden(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrNotFoundData)
            raise models.ErrNotFound(data=data)
        if utils.match_response(http_res, "409", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrConflictData)
            raise models.ErrConflict(data=data)
        if utils.match_response(http_res, "429", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrTooManyRequestsData)
            raise models.ErrTooManyRequests(data=data)
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, models.ErrInternalServerErrorData
            )
            raise models.ErrInternalServerError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def set_override_async(
        self,
        *,
        request: Union[
            models.SetOverrideRequestBody, models.SetOverrideRequestBodyTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SetOverrideResponse:
        r"""
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.SetOverrideRequestBody)
        request = cast(models.SetOverrideRequestBody, request)

        req = self.build_request_async(
            method="POST",
            path="/v1/ratelimits.setOverride",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.SetOverrideRequestBody
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(50, 1000, 1.5, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="setOverride",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "409",
                "429",
                "4XX",
                "500",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.SetOverrideResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.SetOverrideResponseBody]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrBadRequestData)
            raise models.ErrBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrUnauthorizedData)
            raise models.ErrUnauthorized(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrForbiddenData)
            raise models.ErrForbidden(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrNotFoundData)
            raise models.ErrNotFound(data=data)
        if utils.match_response(http_res, "409", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrConflictData)
            raise models.ErrConflict(data=data)
        if utils.match_response(http_res, "429", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrTooManyRequestsData)
            raise models.ErrTooManyRequests(data=data)
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, models.ErrInternalServerErrorData
            )
            raise models.ErrInternalServerError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def list_overrides(
        self,
        *,
        namespace_id: Optional[str] = None,
        namespace_name: Optional[str] = None,
        limit: Optional[int] = 100,
        cursor: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListOverridesResponse:
        r"""
        :param namespace_id:
        :param namespace_name:
        :param limit:
        :param cursor:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListOverridesRequest(
            namespace_id=namespace_id,
            namespace_name=namespace_name,
            limit=limit,
            cursor=cursor,
        )

        req = self.build_request(
            method="GET",
            path="/v1/ratelimits.listOverrides",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(50, 1000, 1.5, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="listOverrides",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "409",
                "429",
                "4XX",
                "500",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.ListOverridesResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.ListOverridesResponseBody]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrBadRequestData)
            raise models.ErrBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrUnauthorizedData)
            raise models.ErrUnauthorized(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrForbiddenData)
            raise models.ErrForbidden(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrNotFoundData)
            raise models.ErrNotFound(data=data)
        if utils.match_response(http_res, "409", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrConflictData)
            raise models.ErrConflict(data=data)
        if utils.match_response(http_res, "429", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrTooManyRequestsData)
            raise models.ErrTooManyRequests(data=data)
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, models.ErrInternalServerErrorData
            )
            raise models.ErrInternalServerError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def list_overrides_async(
        self,
        *,
        namespace_id: Optional[str] = None,
        namespace_name: Optional[str] = None,
        limit: Optional[int] = 100,
        cursor: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ListOverridesResponse:
        r"""
        :param namespace_id:
        :param namespace_name:
        :param limit:
        :param cursor:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListOverridesRequest(
            namespace_id=namespace_id,
            namespace_name=namespace_name,
            limit=limit,
            cursor=cursor,
        )

        req = self.build_request_async(
            method="GET",
            path="/v1/ratelimits.listOverrides",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(50, 1000, 1.5, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="listOverrides",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "409",
                "429",
                "4XX",
                "500",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.ListOverridesResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.ListOverridesResponseBody]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrBadRequestData)
            raise models.ErrBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrUnauthorizedData)
            raise models.ErrUnauthorized(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrForbiddenData)
            raise models.ErrForbidden(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrNotFoundData)
            raise models.ErrNotFound(data=data)
        if utils.match_response(http_res, "409", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrConflictData)
            raise models.ErrConflict(data=data)
        if utils.match_response(http_res, "429", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrTooManyRequestsData)
            raise models.ErrTooManyRequests(data=data)
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, models.ErrInternalServerErrorData
            )
            raise models.ErrInternalServerError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get_override(
        self,
        *,
        identifier: str,
        namespace_id: Optional[str] = None,
        namespace_name: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetOverrideResponse:
        r"""
        :param identifier:
        :param namespace_id:
        :param namespace_name:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetOverrideRequest(
            namespace_id=namespace_id,
            namespace_name=namespace_name,
            identifier=identifier,
        )

        req = self.build_request(
            method="GET",
            path="/v1/ratelimits.getOverride",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(50, 1000, 1.5, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="getOverride",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "409",
                "429",
                "4XX",
                "500",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.GetOverrideResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.GetOverrideResponseBody]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrBadRequestData)
            raise models.ErrBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrUnauthorizedData)
            raise models.ErrUnauthorized(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrForbiddenData)
            raise models.ErrForbidden(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrNotFoundData)
            raise models.ErrNotFound(data=data)
        if utils.match_response(http_res, "409", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrConflictData)
            raise models.ErrConflict(data=data)
        if utils.match_response(http_res, "429", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrTooManyRequestsData)
            raise models.ErrTooManyRequests(data=data)
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, models.ErrInternalServerErrorData
            )
            raise models.ErrInternalServerError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_override_async(
        self,
        *,
        identifier: str,
        namespace_id: Optional[str] = None,
        namespace_name: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetOverrideResponse:
        r"""
        :param identifier:
        :param namespace_id:
        :param namespace_name:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetOverrideRequest(
            namespace_id=namespace_id,
            namespace_name=namespace_name,
            identifier=identifier,
        )

        req = self.build_request_async(
            method="GET",
            path="/v1/ratelimits.getOverride",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(50, 1000, 1.5, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="getOverride",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "403",
                "404",
                "409",
                "429",
                "4XX",
                "500",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.GetOverrideResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.GetOverrideResponseBody]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrBadRequestData)
            raise models.ErrBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrUnauthorizedData)
            raise models.ErrUnauthorized(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrForbiddenData)
            raise models.ErrForbidden(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrNotFoundData)
            raise models.ErrNotFound(data=data)
        if utils.match_response(http_res, "409", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrConflictData)
            raise models.ErrConflict(data=data)
        if utils.match_response(http_res, "429", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrTooManyRequestsData)
            raise models.ErrTooManyRequests(data=data)
        if utils.match_response(http_res, "500", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, models.ErrInternalServerErrorData
            )
            raise models.ErrInternalServerError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
