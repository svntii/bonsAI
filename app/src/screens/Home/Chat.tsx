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
import {
  addMessage,
  getConversation,
} from '../../state/conversation/conversationSlice';
import {ChatScreenRouteProp} from '@T/types';

export default function Chat({route}: {route: ChatScreenRouteProp}) {
  const chatId = route.params.chatId;
  const currentConversation = useAppSelector(
    state => state.conversation.currentConversation,
  );
  const dispatch = useAppDispatch();

  useEffect(() => {
    dispatch(getConversation({id: chatId}));
  }, [chatId, dispatch]);

  const onSend = useCallback(
    (messages: IMessage[] = []) => {
      messages.forEach(message => {
        dispatch(addMessage({conversationId: chatId, message}));
      });
    },
    [dispatch, chatId],
  );

  return (
    <View style={styles.container}>
      <GiftedChat
        messages={currentConversation?.messages}
        onSend={messages => {
          console.log(messages);
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
