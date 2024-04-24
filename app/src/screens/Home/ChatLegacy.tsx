// Chat.tsx

/**
 * TODO:
 *  - Implement a chat window that allows the user to send messages
 *  - The chat window should display the messages sent by the user and the bot
 *  - Implement Redux to manage the state of the chat messages
 *
 *  Currently Only Supports one Chat Store
 */

import {useAppDispatch, useAppSelector} from '@providers/ChatStore';
import React, {useCallback, useEffect} from 'react';
import {View, StyleSheet} from 'react-native';
import {GiftedChat, IMessage} from 'react-native-gifted-chat';
import { addMessage, getConversation} from '../../state/conversation/conversationSlice';
import chatApi from '@api/chatApi';
import initChatApi from '@api/initChatApi';
import {ChatRequestDTO, ChatResponseDTO} from '@api/dto/ChatDTO';


export default function Chat() {
  // const chatId = route.params.chatId;
  const currentConversation = useAppSelector(
    state => state.conversation.currentConversation,
  );
  const chatId = currentConversation.id;
  const dispatch = useAppDispatch();

  useEffect(() => {
    dispatch(getConversation({id: chatId}));
  }, [chatId, dispatch]);

  const receivedMessage = useCallback(
    (message: string) => {
      // call to api to get messages
      const request: ChatRequestDTO = {
        id: chatId,
        prompt: message,
      };

      chatApi
        .postChatMessage(request)
        .then(response => {
          // Handle the response
          // dispatch(addMessage({}))

          dispatch(getConversation({id: chatId}));
        })
        .catch(error => {
          // Handle the error
          console.error(error);
        });
    },
    [dispatch, chatId],
  );

  const onSend = useCallback(
    (messages: IMessage[] = []) => {
      messages.forEach(message => {
        const serializableMessage = {
          ...message,
          createdAt: message.createdAt.valueOf(),
        };
        dispatch(
          addMessage({
            conversationId: chatId,
            message: serializableMessage,
          }),
        );
        dispatch(getConversation({id: chatId}));
      });
    },
    [dispatch, chatId],
  );

  return (
    <View style={styles.container}>
      <GiftedChat
        messages={currentConversation.messages}
        onSend={messages => {
          onSend(messages);
        }}
        user={{
          _id: 1,
        }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
