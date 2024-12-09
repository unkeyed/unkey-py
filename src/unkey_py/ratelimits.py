"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from typing import Any, Optional, Union, cast
from unkey_py import models, utils
from unkey_py._hooks import HookContext
from unkey_py.types import BaseModel, OptionalNullable, UNSET
from unkey_py.utils import get_security_from_env


class Ratelimits(BaseSDK):
    def limit(
        self,
        *,
        request: Union[models.LimitRequestBody, models.LimitRequestBodyTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.LimitResponse:
        r"""
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.LimitRequestBody)
        request = cast(models.LimitRequestBody, request)

        req = self.build_request(
            method="POST",
            path="/v1/ratelimits.limit",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.LimitRequestBody
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
                operation_id="limit",
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
            return models.LimitResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.LimitResponseBody]
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

    async def limit_async(
        self,
        *,
        request: Union[models.LimitRequestBody, models.LimitRequestBodyTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.LimitResponse:
        r"""
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.LimitRequestBody)
        request = cast(models.LimitRequestBody, request)

        req = self.build_request_async(
            method="POST",
            path="/v1/ratelimits.limit",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.LimitRequestBody
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
                operation_id="limit",
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
            return models.LimitResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.LimitResponseBody]
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

    def delete_override(
        self,
        *,
        request: Union[
            models.DeleteOverrideRequestBody, models.DeleteOverrideRequestBodyTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.DeleteOverrideResponse:
        r"""
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.DeleteOverrideRequestBody)
        request = cast(models.DeleteOverrideRequestBody, request)

        req = self.build_request(
            method="POST",
            path="/v1/ratelimits.deleteOverride",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.DeleteOverrideRequestBody
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
                operation_id="deleteOverride",
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
            return models.DeleteOverrideResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.DeleteOverrideResponseBody]
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

    async def delete_override_async(
        self,
        *,
        request: Union[
            models.DeleteOverrideRequestBody, models.DeleteOverrideRequestBodyTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.DeleteOverrideResponse:
        r"""
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.DeleteOverrideRequestBody)
        request = cast(models.DeleteOverrideRequestBody, request)

        req = self.build_request_async(
            method="POST",
            path="/v1/ratelimits.deleteOverride",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.DeleteOverrideRequestBody
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
                operation_id="deleteOverride",
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
            return models.DeleteOverrideResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[models.DeleteOverrideResponseBody]
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
