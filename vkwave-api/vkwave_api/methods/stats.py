from vkwave_types.responses import *
from ._category import Category


class Stats(Category):
    def get(
        self,
        group_id: typing.Optional[int],
        app_id: typing.Optional[int],
        timestamp_from: typing.Optional[int],
        timestamp_to: typing.Optional[int],
        interval: typing.Optional[str],
        intervals_count: typing.Optional[int],
        filters: typing.Optional[typing.List[str]],
        stats_groups: typing.Optional[typing.List[str]],
        extended: typing.Optional[bool],
    ) -> StatsGetResponse:
        """
        :param group_id: - Community ID.
        :param app_id: - Application ID.
        :param timestamp_from:
        :param timestamp_to:
        :param interval:
        :param intervals_count:
        :param filters:
        :param stats_groups:
        :param extended:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = StatsGetResponse(**raw_result)
        return result

    def get_post_reach(
        self, owner_id: typing.Optional[str], post_id: typing.Optional[int],
    ) -> StatsGetPostReachResponse:
        """
        :param owner_id: - post owner community id. Specify with "-" sign.
        :param post_id: - wall post id. Note that stats are available only for '300' last (newest) posts on a community wall.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getPostReach", params)
        result = StatsGetPostReachResponse(**raw_result)
        return result

    def track_visitor(self, id: typing.Optional[str],) -> OkResponse:
        """
        :param id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("trackVisitor", params)
        result = OkResponse(**raw_result)
        return result
