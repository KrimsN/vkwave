from vkwave_types.responses import *
from ._category import Category


class Leads(Category):
    def check_user(
        self,
        lead_id: typing.Optional[int],
        test_result: typing.Optional[int],
        test_mode: typing.Optional[bool],
        auto_start: typing.Optional[bool],
        age: typing.Optional[int],
        country: typing.Optional[str],
    ) -> LeadsCheckUserResponse:
        """
        :param lead_id: - Lead ID.
        :param test_result: - Value to be return in 'result' field when test mode is used.
        :param test_mode:
        :param auto_start:
        :param age: - User age.
        :param country: - User country code.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("checkUser", params)
        result = LeadsCheckUserResponse(**raw_result)
        return result

    def complete(
        self,
        vk_sid: typing.Optional[str],
        secret: typing.Optional[str],
        comment: typing.Optional[str],
    ) -> LeadsCompleteResponse:
        """
        :param vk_sid: - Session obtained as GET parameter when session started.
        :param secret: - Secret key from the lead testing interface.
        :param comment: - Comment text.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("complete", params)
        result = LeadsCompleteResponse(**raw_result)
        return result

    def get_stats(
        self,
        lead_id: typing.Optional[int],
        secret: typing.Optional[str],
        date_start: typing.Optional[str],
        date_end: typing.Optional[str],
    ) -> LeadsGetStatsResponse:
        """
        :param lead_id: - Lead ID.
        :param secret: - Secret key obtained from the lead testing interface.
        :param date_start: - Day to start stats from (YYYY_MM_DD, e.g.2011-09-17).
        :param date_end: - Day to finish stats (YYYY_MM_DD, e.g.2011-09-17).
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getStats", params)
        result = LeadsGetStatsResponse(**raw_result)
        return result

    def get_users(
        self,
        offer_id: typing.Optional[int],
        secret: typing.Optional[str],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        status: typing.Optional[int],
        reverse: typing.Optional[bool],
    ) -> LeadsGetUsersResponse:
        """
        :param offer_id: - Offer ID.
        :param secret: - Secret key obtained in the lead testing interface.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of results to return.
        :param status: - Action type. Possible values: *'0' — start,, *'1' — finish,, *'2' — blocking users,, *'3' — start in a test mode,, *'4' — finish in a test mode.
        :param reverse: - Sort order. Possible values: *'1' — chronological,, *'0' — reverse chronological.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getUsers", params)
        result = LeadsGetUsersResponse(**raw_result)
        return result

    def metric_hit(self, data: typing.Optional[str],) -> LeadsMetricHitResponse:
        """
        :param data: - Metric data obtained in the lead interface.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("metricHit", params)
        result = LeadsMetricHitResponse(**raw_result)
        return result

    def start(
        self,
        lead_id: typing.Optional[int],
        secret: typing.Optional[str],
        uid: typing.Optional[int],
        aid: typing.Optional[int],
        test_mode: typing.Optional[bool],
        force: typing.Optional[bool],
    ) -> LeadsStartResponse:
        """
        :param lead_id: - Lead ID.
        :param secret: - Secret key from the lead testing interface.
        :param uid:
        :param aid:
        :param test_mode:
        :param force:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("start", params)
        result = LeadsStartResponse(**raw_result)
        return result
