import React, { useEffect } from 'react';
import { View, StyleSheet } from 'react-native';
import { GiftedChat, IMessage } from 'react-native-gifted-chat';
import { useAppDispatch, useAppSelector } from '@providers/ChatStore';
import { addMessage, getConversation } from '../../state/conversation/conversationSlice';
import chatApi from '@api/chatApi';
import initChatApi from '@api/initChatApi';
import { ChatRequestDTO, ChatResponseDTO, initChatResponseDTO } from '@api/dto/ChatDTO';
import { initialize } from 'parse';

export default function Chat() {
  const currentConversation = useAppSelector(state => state.conversation.currentConversation);
  const chatId = currentConversation.id;
  const dispatch = useAppDispatch();

  useEffect(() => {
    async function initializeChat() {
      try {
        const response: initChatResponseDTO = await initChatApi.postChatMessage();
        const currentDate = new Date();
        const serializedDate = currentDate.toISOString();
        onSend([
          {
            _id: chatId, // Use a unique ID for the message
            text: response.response,
            createdAt: currentDate,
            user: { _id: 1 }, // Set the user ID to represent the opponent (e.g., ID 2)
          }
        ]);
      } catch (error) {
        console.error('Error initializing chat API:', error);
      }
    }
    initializeChat(); // Call the initialization function when the component mounts
  }, []);


  const onSend = (messages: IMessage[] = []) => {
    messages.forEach(message => {
      const serializableMessage = {
        ...message,
        createdAt: message.createdAt.valueOf(),
      };
      dispatch(addMessage({ conversationId: chatId, message: serializableMessage }));
      dispatch(getConversation({ id: chatId }));
    });
  };

  return (
    <View style={styles.container}>
      <GiftedChat
        messages={currentConversation.messages}
        onSend={onSend}
        user={{ _id: 2 }} // Set the user ID to represent the current user (e.g., ID 1)
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
