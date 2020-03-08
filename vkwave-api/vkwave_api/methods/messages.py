from vkwave_types.responses import *
from ._category import Category


class Messages(Category):
    def add_chat_user(
        self, chat_id: typing.Optional[int], user_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param chat_id: - Chat ID.
        :param user_id: - ID of the user to be added to the chat.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addChatUser", params)
        result = OkResponse(**raw_result)
        return result

    def allow_messages_from_group(
        self, group_id: typing.Optional[int], key: typing.Optional[str],
    ) -> OkResponse:
        """
        :param group_id: - Group ID.
        :param key:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("allowMessagesFromGroup", params)
        result = OkResponse(**raw_result)
        return result

    def create_chat(
        self, user_ids: typing.Optional[typing.List[int]], title: typing.Optional[str],
    ) -> MessagesCreateChatResponse:
        """
        :param user_ids: - IDs of the users to be added to the chat.
        :param title: - Chat title.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createChat", params)
        result = MessagesCreateChatResponse(**raw_result)
        return result

    def delete(
        self,
        message_ids: typing.Optional[typing.List[int]],
        spam: typing.Optional[bool],
        group_id: typing.Optional[int],
        delete_for_all: typing.Optional[bool],
    ) -> MessagesDeleteResponse:
        """
        :param message_ids: - Message IDs.
        :param spam: - '1' — to mark message as spam.
        :param group_id: - Group ID (for group messages with user access token)
        :param delete_for_all: - '1' — delete message for for all.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("delete", params)
        result = MessagesDeleteResponse(**raw_result)
        return result

    def delete_chat_photo(
        self, chat_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> MessagesDeleteChatPhotoResponse:
        """
        :param chat_id: - Chat ID.
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteChatPhoto", params)
        result = MessagesDeleteChatPhotoResponse(**raw_result)
        return result

    def delete_conversation(
        self,
        user_id: typing.Optional[int],
        peer_id: typing.Optional[int],
        group_id: typing.Optional[int],
    ) -> MessagesDeleteConversationResponse:
        """
        :param user_id: - User ID. To clear a chat history use 'chat_id'
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: - Group ID (for group messages with user access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteConversation", params)
        result = MessagesDeleteConversationResponse(**raw_result)
        return result

    def deny_messages_from_group(self, group_id: typing.Optional[int],) -> OkResponse:
        """
        :param group_id: - Group ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("denyMessagesFromGroup", params)
        result = OkResponse(**raw_result)
        return result

    def edit(
        self,
        peer_id: typing.Optional[int],
        message: typing.Optional[str],
        message_id: typing.Optional[int],
        lat: typing.Optional[int],
        long: typing.Optional[int],
        attachment: typing.Optional[str],
        keep_forward_messages: typing.Optional[bool],
        keep_snippets: typing.Optional[bool],
        group_id: typing.Optional[int],
        dont_parse_links: typing.Optional[bool],
    ) -> MessagesEditResponse:
        """
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param message: - (Required if 'attachments' is not set.) Text of the message.
        :param message_id:
        :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: - (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param keep_forward_messages: - '1' — to keep forwarded, messages.
        :param keep_snippets: - '1' — to keep attached snippets.
        :param group_id: - Group ID (for group messages with user access token)
        :param dont_parse_links:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("edit", params)
        result = MessagesEditResponse(**raw_result)
        return result

    def edit_chat(
        self, chat_id: typing.Optional[int], title: typing.Optional[str],
    ) -> OkResponse:
        """
        :param chat_id: - Chat ID.
        :param title: - New title of the chat.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editChat", params)
        result = OkResponse(**raw_result)
        return result

    def get_by_conversation_message_id(
        self,
        peer_id: typing.Optional[int],
        conversation_message_ids: typing.Optional[typing.List[int]],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[UsersFields]],
        group_id: typing.Optional[int],
    ) -> MessagesGetByConversationMessageIdResponse:
        """
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param conversation_message_ids: - Conversation message IDs.
        :param extended: - Information whether the response should be extended
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getByConversationMessageId", params)
        result = MessagesGetByConversationMessageIdResponse(**raw_result)
        return result

    def get_by_id(
        self,
        message_ids: typing.Optional[typing.List[int]],
        preview_length: typing.Optional[int],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[UsersFields]],
        group_id: typing.Optional[int],
    ) -> MessagesGetByIdResponse:
        """
        :param message_ids: - Message IDs.
        :param preview_length: - Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param extended: - Information whether the response should be extended
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getById", params)
        result = MessagesGetByIdResponse(**raw_result)
        return result

    def get_chat_preview(
        self,
        peer_id: typing.Optional[int],
        link: typing.Optional[str],
        fields: typing.Optional[typing.List[UsersFields]],
    ) -> MessagesGetChatPreviewResponse:
        """
        :param peer_id:
        :param link: - Invitation link.
        :param fields: - Profile fields to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getChatPreview", params)
        result = MessagesGetChatPreviewResponse(**raw_result)
        return result

    def get_conversation_members(
        self,
        peer_id: typing.Optional[int],
        fields: typing.Optional[typing.List[UsersFields]],
        group_id: typing.Optional[int],
    ) -> MessagesGetConversationMembersResponse:
        """
        :param peer_id: - Peer ID.
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getConversationMembers", params)
        result = MessagesGetConversationMembersResponse(**raw_result)
        return result

    def get_conversations(
        self,
        offset: typing.Optional[int],
        count: typing.Optional[int],
        filter: typing.Optional[str],
        extended: typing.Optional[bool],
        start_message_id: typing.Optional[int],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
        group_id: typing.Optional[int],
    ) -> MessagesGetConversationsResponse:
        """
        :param offset: - Offset needed to return a specific subset of conversations.
        :param count: - Number of conversations to return.
        :param filter: - Filter to apply: 'all' — all conversations, 'unread' — conversations with unread messages, 'important' — conversations, marked as important (only for community messages), 'unanswered' — conversations, marked as unanswered (only for community messages)
        :param extended: - '1' — return extra information about users and communities
        :param start_message_id: - ID of the message from what to return dialogs.
        :param fields: - Profile and communities fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getConversations", params)
        result = MessagesGetConversationsResponse(**raw_result)
        return result

    def get_conversations_by_id(
        self,
        peer_ids: typing.Optional[typing.List[int]],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
        group_id: typing.Optional[int],
    ) -> MessagesGetConversationsByIdResponse:
        """
        :param peer_ids: - Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: - Return extended properties
        :param fields: - Profile and communities fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getConversationsById", params)
        result = MessagesGetConversationsByIdResponse(**raw_result)
        return result

    def get_history(
        self,
        offset: typing.Optional[int],
        count: typing.Optional[int],
        user_id: typing.Optional[int],
        peer_id: typing.Optional[int],
        start_message_id: typing.Optional[int],
        rev: typing.Optional[int],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[UsersFields]],
        group_id: typing.Optional[int],
    ) -> MessagesGetHistoryResponse:
        """
        :param offset: - Offset needed to return a specific subset of messages.
        :param count: - Number of messages to return.
        :param user_id: - ID of the user whose message history you want to return.
        :param peer_id:
        :param start_message_id: - Starting message ID from which to return history.
        :param rev: - Sort order: '1' — return messages in chronological order. '0' — return messages in reverse chronological order.
        :param extended: - Information whether the response should be extended
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getHistory", params)
        result = MessagesGetHistoryResponse(**raw_result)
        return result

    def get_history_attachments(
        self,
        peer_id: typing.Optional[int],
        media_type: typing.Optional[str],
        start_from: typing.Optional[str],
        count: typing.Optional[int],
        photo_sizes: typing.Optional[bool],
        fields: typing.Optional[typing.List[UsersFields]],
        group_id: typing.Optional[int],
        preserve_order: typing.Optional[bool],
        max_forwards_level: typing.Optional[int],
    ) -> MessagesGetHistoryAttachmentsResponse:
        """
        :param peer_id: - Peer ID. ", For group chat: '2000000000 + chat ID' , , For community: '-community ID'"
        :param media_type: - Type of media files to return: *'photo',, *'video',, *'audio',, *'doc',, *'link'.,*'market'.,*'wall'.,*'share'
        :param start_from: - Message ID to start return results from.
        :param count: - Number of objects to return.
        :param photo_sizes: - '1' — to return photo sizes in a
        :param fields: - Additional profile [vk.com/dev/fields|fields] to return. 
        :param group_id: - Group ID (for group messages with group access token)
        :param preserve_order:
        :param max_forwards_level:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getHistoryAttachments", params)
        result = MessagesGetHistoryAttachmentsResponse(**raw_result)
        return result

    def get_invite_link(
        self,
        peer_id: typing.Optional[int],
        reset: typing.Optional[bool],
        group_id: typing.Optional[int],
    ) -> MessagesGetInviteLinkResponse:
        """
        :param peer_id: - Destination ID.
        :param reset: - 1 — to generate new link (revoke previous), 0 — to return previous link.
        :param group_id: - Group ID
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getInviteLink", params)
        result = MessagesGetInviteLinkResponse(**raw_result)
        return result

    def get_last_activity(
        self, user_id: typing.Optional[int],
    ) -> MessagesGetLastActivityResponse:
        """
        :param user_id: - User ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getLastActivity", params)
        result = MessagesGetLastActivityResponse(**raw_result)
        return result

    def get_long_poll_history(
        self,
        ts: typing.Optional[int],
        pts: typing.Optional[int],
        preview_length: typing.Optional[int],
        onlines: typing.Optional[bool],
        fields: typing.Optional[typing.List[UsersFields]],
        events_limit: typing.Optional[int],
        msgs_limit: typing.Optional[int],
        max_msg_id: typing.Optional[int],
        group_id: typing.Optional[int],
        lp_version: typing.Optional[int],
        last_n: typing.Optional[int],
        credentials: typing.Optional[bool],
    ) -> MessagesGetLongPollHistoryResponse:
        """
        :param ts: - Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param pts: - Lsat value of 'pts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param preview_length: - Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param onlines: - '1' — to return history with online users only.
        :param fields: - Additional profile [vk.com/dev/fields|fields] to return.
        :param events_limit: - Maximum number of events to return.
        :param msgs_limit: - Maximum number of messages to return.
        :param max_msg_id: - Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
        :param group_id: - Group ID (for group messages with user access token)
        :param lp_version:
        :param last_n:
        :param credentials:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getLongPollHistory", params)
        result = MessagesGetLongPollHistoryResponse(**raw_result)
        return result

    def get_long_poll_server(
        self,
        need_pts: typing.Optional[bool],
        group_id: typing.Optional[int],
        lp_version: typing.Optional[int],
    ) -> MessagesGetLongPollServerResponse:
        """
        :param need_pts: - '1' — to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param group_id: - Group ID (for group messages with user access token)
        :param lp_version: - Long poll version
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getLongPollServer", params)
        result = MessagesGetLongPollServerResponse(**raw_result)
        return result

    def is_messages_from_group_allowed(
        self, group_id: typing.Optional[int], user_id: typing.Optional[int],
    ) -> MessagesIsMessagesFromGroupAllowedResponse:
        """
        :param group_id: - Group ID.
        :param user_id: - User ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("isMessagesFromGroupAllowed", params)
        result = MessagesIsMessagesFromGroupAllowedResponse(**raw_result)
        return result

    def join_chat_by_invite_link(
        self, link: typing.Optional[str],
    ) -> MessagesJoinChatByInviteLinkResponse:
        """
        :param link: - Invitation link.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("joinChatByInviteLink", params)
        result = MessagesJoinChatByInviteLinkResponse(**raw_result)
        return result

    def mark_as_answered_conversation(
        self,
        peer_id: typing.Optional[int],
        answered: typing.Optional[bool],
        group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param peer_id: - ID of conversation to mark as important.
        :param answered: - '1' — to mark as answered, '0' — to remove the mark
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("markAsAnsweredConversation", params)
        result = OkResponse(**raw_result)
        return result

    def mark_as_important(
        self,
        message_ids: typing.Optional[typing.List[int]],
        important: typing.Optional[int],
    ) -> MessagesMarkAsImportantResponse:
        """
        :param message_ids: - IDs of messages to mark as important.
        :param important: - '1' — to add a star (mark as important), '0' — to remove the star
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("markAsImportant", params)
        result = MessagesMarkAsImportantResponse(**raw_result)
        return result

    def mark_as_important_conversation(
        self,
        peer_id: typing.Optional[int],
        important: typing.Optional[bool],
        group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param peer_id: - ID of conversation to mark as important.
        :param important: - '1' — to add a star (mark as important), '0' — to remove the star
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("markAsImportantConversation", params)
        result = OkResponse(**raw_result)
        return result

    def mark_as_read(
        self,
        message_ids: typing.Optional[typing.List[int]],
        peer_id: typing.Optional[int],
        start_message_id: typing.Optional[int],
        group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param message_ids: - IDs of messages to mark as read.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: - Message ID to start from.
        :param group_id: - Group ID (for group messages with user access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("markAsRead", params)
        result = OkResponse(**raw_result)
        return result

    def pin(
        self, peer_id: typing.Optional[int], message_id: typing.Optional[int],
    ) -> MessagesPinResponse:
        """
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param message_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("pin", params)
        result = MessagesPinResponse(**raw_result)
        return result

    def remove_chat_user(
        self,
        chat_id: typing.Optional[int],
        user_id: typing.Optional[int],
        member_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param chat_id: - Chat ID.
        :param user_id: - ID of the user to be removed from the chat.
        :param member_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeChatUser", params)
        result = OkResponse(**raw_result)
        return result

    def restore(
        self, message_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param message_id: - ID of a previously-deleted message to restore.
        :param group_id: - Group ID (for group messages with user access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("restore", params)
        result = OkResponse(**raw_result)
        return result

    def search(
        self,
        q: typing.Optional[str],
        peer_id: typing.Optional[int],
        date: typing.Optional[int],
        preview_length: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[str]],
        group_id: typing.Optional[int],
    ) -> MessagesSearchResponse:
        """
        :param q: - Search query string.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param date: - Date to search message before in Unixtime.
        :param preview_length: - Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param offset: - Offset needed to return a specific subset of messages.
        :param count: - Number of messages to return.
        :param extended:
        :param fields:
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("search", params)
        result = MessagesSearchResponse(**raw_result)
        return result

    def search_conversations(
        self,
        q: typing.Optional[str],
        count: typing.Optional[int],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[UsersFields]],
        group_id: typing.Optional[int],
    ) -> MessagesSearchConversationsResponse:
        """
        :param q: - Search query string.
        :param count: - Maximum number of results.
        :param extended: - '1' — return extra information about users and communities
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with user access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("searchConversations", params)
        result = MessagesSearchConversationsResponse(**raw_result)
        return result

    def send(
        self,
        user_id: typing.Optional[int],
        random_id: typing.Optional[int],
        peer_id: typing.Optional[int],
        domain: typing.Optional[str],
        chat_id: typing.Optional[int],
        user_ids: typing.Optional[typing.List[int]],
        message: typing.Optional[str],
        lat: typing.Optional[int],
        long: typing.Optional[int],
        attachment: typing.Optional[str],
        reply_to: typing.Optional[int],
        forward_messages: typing.Optional[typing.List[int]],
        forward: typing.Optional[str],
        sticker_id: typing.Optional[int],
        group_id: typing.Optional[int],
        keyboard: typing.Optional[str],
        payload: typing.Optional[str],
        dont_parse_links: typing.Optional[bool],
        disable_mentions: typing.Optional[bool],
    ) -> MessagesSendResponse:
        """
        :param user_id: - User ID (by default — current user).
        :param random_id: - Unique identifier to avoid resending the message.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param domain: - User's short address (for example, 'illarionov').
        :param chat_id: - ID of conversation the message will relate to.
        :param user_ids: - IDs of message recipients (if new conversation shall be started).
        :param message: - (Required if 'attachments' is not set.) Text of the message.
        :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: - (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param reply_to:
        :param forward_messages: - ID of forwarded messages, separated with a comma. Listed messages of the sender will be shown in the message body at the recipient's. Example: "123,431,544"
        :param forward:
        :param sticker_id: - Sticker id.
        :param group_id: - Group ID (for group messages with group access token)
        :param keyboard:
        :param payload:
        :param dont_parse_links:
        :param disable_mentions:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("send", params)
        result = MessagesSendResponse(**raw_result)
        return result

    def set_activity(
        self,
        user_id: typing.Optional[int],
        type: typing.Optional[str],
        peer_id: typing.Optional[int],
        group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param user_id: - User ID.
        :param type: - 'typing' — user has started to type.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: - Group ID (for group messages with group access token)
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("setActivity", params)
        result = OkResponse(**raw_result)
        return result

    def set_chat_photo(
        self, file: typing.Optional[str],
    ) -> MessagesSetChatPhotoResponse:
        """
        :param file: - Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("setChatPhoto", params)
        result = MessagesSetChatPhotoResponse(**raw_result)
        return result

    def unpin(
        self, peer_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param peer_id:
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("unpin", params)
        result = OkResponse(**raw_result)
        return result
