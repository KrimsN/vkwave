from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Orders(Category):
    async def cancel_subscription(
        self,
        user_id: int = None,
        subscription_id: int = None,
        pending_cancel: typing.Optional[bool] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OrdersCancelSubscriptionResponse]:
        """
        :param user_id:
        :param subscription_id:
        :param pending_cancel:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("cancelSubscription", params)
        if raw:
            return raw_result

        result = OrdersCancelSubscriptionResponse(**raw_result)
        return result

    async def change_state(
        self,
        order_id: int = None,
        action: str = None,
        app_order_id: typing.Optional[int] = None,
        test_mode: typing.Optional[BaseBoolInt] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OrdersChangeStateResponse]:
        """
        :param order_id: - order ID.
        :param action: - action to be done with the order. Available actions: *cancel — to cancel unconfirmed order. *charge — to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund — to cancel confirmed order.
        :param app_order_id: - internal ID of the order in the application.
        :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("changeState", params)
        if raw:
            return raw_result

        result = OrdersChangeStateResponse(**raw_result)
        return result

    async def get(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        test_mode: typing.Optional[BaseBoolInt] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OrdersGetResponse]:
        """
        :param offset:
        :param count: - number of returned orders.
        :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if raw:
            return raw_result

        result = OrdersGetResponse(**raw_result)
        return result

    async def get_amount(
        self, user_id: int = None, votes: typing.List[str] = None, raw: bool = False,
    ) -> typing.Union[dict, OrdersGetAmountResponse]:
        """
        :param user_id:
        :param votes:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAmount", params)
        if raw:
            return raw_result

        result = OrdersGetAmountResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        order_id: typing.Optional[int] = None,
        order_ids: typing.Optional[typing.List[int]] = None,
        test_mode: typing.Optional[BaseBoolInt] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OrdersGetByIdResponse]:
        """
        :param order_id: - order ID.
        :param order_ids: - order IDs (when information about several orders is requested).
        :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if raw:
            return raw_result

        result = OrdersGetByIdResponse(**raw_result)
        return result

    async def get_user_subscription_by_id(
        self, user_id: int = None, subscription_id: int = None, raw: bool = False,
    ) -> typing.Union[dict, OrdersGetUserSubscriptionByIdResponse]:
        """
        :param user_id:
        :param subscription_id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUserSubscriptionById", params)
        if raw:
            return raw_result

        result = OrdersGetUserSubscriptionByIdResponse(**raw_result)
        return result

    async def get_user_subscriptions(
        self, user_id: int = None, raw: bool = False,
    ) -> typing.Union[dict, OrdersGetUserSubscriptionsResponse]:
        """
        :param user_id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUserSubscriptions", params)
        if raw:
            return raw_result

        result = OrdersGetUserSubscriptionsResponse(**raw_result)
        return result

    async def update_subscription(
        self,
        user_id: int = None,
        subscription_id: int = None,
        price: int = None,
        raw: bool = False,
    ) -> typing.Union[dict, OrdersUpdateSubscriptionResponse]:
        """
        :param user_id:
        :param subscription_id:
        :param price:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("updateSubscription", params)
        if raw:
            return raw_result

        result = OrdersUpdateSubscriptionResponse(**raw_result)
        return result