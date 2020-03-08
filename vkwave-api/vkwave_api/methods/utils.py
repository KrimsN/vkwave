from vkwave_types.responses import *
from ._category import Category


class Utils(Category):
    def check_link(self, url: typing.Optional[str],) -> UtilsCheckLinkResponse:
        """
        :param url: - Link to check (e.g., 'http://google.com').
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("checkLink", params)
        result = UtilsCheckLinkResponse(**raw_result)
        return result

    def delete_from_last_shortened(self, key: typing.Optional[str],) -> OkResponse:
        """
        :param key: - Link key (characters after vk.cc/).
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteFromLastShortened", params)
        result = OkResponse(**raw_result)
        return result

    def get_last_shortened_links(
        self, count: typing.Optional[int], offset: typing.Optional[int],
    ) -> UtilsGetLastShortenedLinksResponse:
        """
        :param count: - Number of links to return.
        :param offset: - Offset needed to return a specific subset of links.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getLastShortenedLinks", params)
        result = UtilsGetLastShortenedLinksResponse(**raw_result)
        return result

    def get_link_stats(
        self,
        key: typing.Optional[str],
        source: typing.Optional[str],
        access_key: typing.Optional[str],
        interval: typing.Optional[str],
        intervals_count: typing.Optional[int],
        extended: typing.Optional[bool],
    ) -> UtilsGetLinkStatsResponse:
        """
        :param key: - Link key (characters after vk.cc/).
        :param source: - Source of scope
        :param access_key: - Access key for private link stats.
        :param interval: - Interval.
        :param intervals_count: - Number of intervals to return.
        :param extended: - 1 — to return extended stats data (sex, age, geo). 0 — to return views number only.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getLinkStats", params)
        result = UtilsGetLinkStatsResponse(**raw_result)
        return result

    def get_server_time(self,) -> UtilsGetServerTimeResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getServerTime", params)
        result = UtilsGetServerTimeResponse(**raw_result)
        return result

    def get_short_link(
        self, url: typing.Optional[str], private: typing.Optional[bool],
    ) -> UtilsGetShortLinkResponse:
        """
        :param url: - URL to be shortened.
        :param private: - 1 — private stats, 0 — public stats.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getShortLink", params)
        result = UtilsGetShortLinkResponse(**raw_result)
        return result

    def resolve_screen_name(
        self, screen_name: typing.Optional[str],
    ) -> UtilsResolveScreenNameResponse:
        """
        :param screen_name: - Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("resolveScreenName", params)
        result = UtilsResolveScreenNameResponse(**raw_result)
        return result
