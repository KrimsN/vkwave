from vkwave_types.responses import *
from ._category import Category


class Stories(Category):
    def ban_owner(self, owners_ids: typing.Optional[typing.List[int]],) -> OkResponse:
        """
        :param owners_ids: - List of sources IDs
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("banOwner", params)
        result = OkResponse(**raw_result)
        return result

    def delete(
        self, owner_id: typing.Optional[int], story_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - Story owner's ID. Current user id is used by default.
        :param story_id: - Story ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("delete", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self, owner_id: typing.Optional[int], extended: typing.Optional[bool],
    ) -> StoriesGetResponse:
        """
        :param owner_id: - Owner ID.
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = StoriesGetResponse(**raw_result)
        return result

    def get_banned(
        self,
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
    ) -> StoriesGetBannedResponse:
        """
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: - Additional fields to return
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getBanned", params)
        result = StoriesGetBannedResponse(**raw_result)
        return result

    def get_by_id(
        self,
        stories: typing.Optional[typing.List[str]],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
    ) -> StoriesGetByIdResponse:
        """
        :param stories: - Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: - Additional fields to return
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getById", params)
        result = StoriesGetByIdResponse(**raw_result)
        return result

    def get_photo_upload_server(
        self,
        add_to_news: typing.Optional[bool],
        user_ids: typing.Optional[typing.List[int]],
        reply_to_story: typing.Optional[str],
        link_text: typing.Optional[str],
        link_url: typing.Optional[str],
        group_id: typing.Optional[int],
    ) -> StoriesGetPhotoUploadServerResponse:
        """
        :param add_to_news: - 1 — to add the story to friend's feed.
        :param user_ids: - List of users IDs who can see the story.
        :param reply_to_story: - ID of the story to reply with the current.
        :param link_text: - Link text (for community's stories only).
        :param link_url: - Link URL. Internal links on https://vk.com only.
        :param group_id: - ID of the community to upload the story (should be verified or with the "fire" icon).
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getPhotoUploadServer", params)
        result = StoriesGetPhotoUploadServerResponse(**raw_result)
        return result

    def get_replies(
        self,
        owner_id: typing.Optional[int],
        story_id: typing.Optional[int],
        access_key: typing.Optional[str],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
    ) -> StoriesGetRepliesResponse:
        """
        :param owner_id: - Story owner ID.
        :param story_id: - Story ID.
        :param access_key: - Access key for the private object.
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: - Additional fields to return
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getReplies", params)
        result = StoriesGetRepliesResponse(**raw_result)
        return result

    def get_stats(
        self, owner_id: typing.Optional[int], story_id: typing.Optional[int],
    ) -> StoriesGetStatsResponse:
        """
        :param owner_id: - Story owner ID. 
        :param story_id: - Story ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getStats", params)
        result = StoriesGetStatsResponse(**raw_result)
        return result

    def get_video_upload_server(
        self,
        add_to_news: typing.Optional[bool],
        user_ids: typing.Optional[typing.List[int]],
        reply_to_story: typing.Optional[str],
        link_text: typing.Optional[str],
        link_url: typing.Optional[str],
        group_id: typing.Optional[int],
    ) -> StoriesGetVideoUploadServerResponse:
        """
        :param add_to_news: - 1 — to add the story to friend's feed.
        :param user_ids: - List of users IDs who can see the story.
        :param reply_to_story: - ID of the story to reply with the current.
        :param link_text: - Link text (for community's stories only).
        :param link_url: - Link URL. Internal links on https://vk.com only.
        :param group_id: - ID of the community to upload the story (should be verified or with the "fire" icon).
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getVideoUploadServer", params)
        result = StoriesGetVideoUploadServerResponse(**raw_result)
        return result

    def get_viewers(
        self,
        owner_id: typing.Optional[int],
        story_id: typing.Optional[int],
        count: typing.Optional[int],
        offset: typing.Optional[int],
        extended: typing.Optional[bool],
    ) -> StoriesGetViewersResponse:
        """
        :param owner_id: - Story owner ID.
        :param story_id: - Story ID.
        :param count: - Maximum number of results.
        :param offset: - Offset needed to return a specific subset of results.
        :param extended: - '1' — to return detailed information about photos
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getViewers", params)
        result = StoriesGetViewersResponse(**raw_result)
        return result

    def hide_all_replies(
        self, owner_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user whose replies should be hidden.
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("hideAllReplies", params)
        result = OkResponse(**raw_result)
        return result

    def hide_reply(
        self, owner_id: typing.Optional[int], story_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user whose replies should be hidden.
        :param story_id: - Story ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("hideReply", params)
        result = OkResponse(**raw_result)
        return result

    def unban_owner(self, owners_ids: typing.Optional[typing.List[int]],) -> OkResponse:
        """
        :param owners_ids: - List of hidden sources to show stories from.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("unbanOwner", params)
        result = OkResponse(**raw_result)
        return result
