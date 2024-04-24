import React, { useEffect } from 'react';
import { View, StyleSheet, Button, TextInput, Text, TouchableOpacity } from 'react-native';
import { GiftedChat, IMessage } from 'react-native-gifted-chat';
import { useAppDispatch, useAppSelector } from '@providers/ChatStore';
import { addMessage, getConversation } from '../../state/conversation/conversationSlice';
import chatApi from '@api/chatApi';
import initChatApi from '@api/initChatApi';
import { ChatRequestDTO, ChatResponseDTO, initChatResponseDTO } from '@api/dto/ChatDTO';

export default function Chat() {
  const currentConversation = useAppSelector(state => state.conversation.currentConversation);
  const internalId = currentConversation.internalId;
  const dispatch = useAppDispatch();

  useEffect(() => {
    async function initializeChat() {
      try {
        const response: initChatResponseDTO = await initChatApi.postChatMessage();
        handleSendResponse(response.response, 0); // Send the initial response to the chat (from the bot)
        currentConversation.backendId = response.id;
      } catch (error) {
        console.error('Error initializing chat API:', error);
      }
    }
    initializeChat(); // Call the initialization function when the component mounts
  }, []);

  async function requestChatResponse(lastMessage: IMessage) {
    try {
      const request: ChatRequestDTO = {
        id: currentConversation.backendId,
        prompt: lastMessage.text,
      };
      const response: ChatResponseDTO = await chatApi.postChatMessage(request);
      handleSendResponse(response.response, 0); // Send the bot's response to the chat
    }
    catch (error) {
      console.error('Error requesting chat response:', error);
    }
  }
  
  const handleSendResponse = async (text: string, userId: number) => {
    try {
      const currentDate = new Date();
      const serializedDate = currentDate.toISOString();
      const timestamp = Date.now();
      const messageId = 'user' + internalId + '_' + timestamp;
      const message: IMessage = {
        _id: messageId, // Use a unique ID for the message
        text: text,
        createdAt: serializedDate,
        user: { _id: userId }, // Set the user ID to represent the current user
      };
  
      if (userId !== 0) {
        await onSend([message]);
      } else {
        await displayMessages([message]);
      }
    } catch (error) {
      console.error('Error handling send response:', error);
    }
  };
  
  const displayMessages = async (messages: IMessage[] = []) => {
    try {
      const promises = messages.map(async (message) => {
        const serializableMessage = {
          ...message,
          createdAt: message.createdAt.valueOf(),
        };
        await dispatch(addMessage({ internalId: internalId, message: serializableMessage }));
      });
      await Promise.all(promises);
      await dispatch(getConversation({ internalId: internalId }));
    } catch (error) {
      console.error('Error displaying messages:', error);
    }
  };
  
  const onSend = async (messages: IMessage[] = []) => {
    try {
      await displayMessages(messages);
      await requestChatResponse(messages[messages.length - 1]); // only basing responses off the last user message
    } catch (error) {
      console.error('Error on send:', error);
    }
  };
  

  // user response suggestions
  const CustomComposer = (props) => (
    <View style={{ flex: 1 }}>
      <View style={{ flexDirection: 'row', justifyContent: 'space-around', padding: 5 }}>
        {/* Example response suggestion buttons */}
        <TouchableOpacity
          style={{ backgroundColor: 'green', padding: 10, borderRadius: 10 }}
          onPress={() => handleSendResponse('Yes', internalId)}
        >
          <Text style={{ color: 'white' }}>Yes</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={{ backgroundColor: 'green', padding: 10, borderRadius: 10 }}
          onPress={() => handleSendResponse('No', internalId)}
        >
          <Text style={{ color: 'white' }}>No</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={{ backgroundColor: 'green', padding: 10, borderRadius: 10 }}
          onPress={() => handleSendResponse('Maybe', internalId)}
        >
          <Text style={{ color: 'white' }}>Maybe</Text>
        </TouchableOpacity>
      </View>
      <TextInput
        {...props}
        placeholder="Type a message..."
        multiline={true}
        style={{ flex: 1, minHeight: 40, borderWidth: 1, borderColor: '#ccc', padding: 10 }}
      />
    </View>
  );
  

  return (
    <View style={styles.container}>
      <GiftedChat
        messages={currentConversation.messages}
        onSend={onSend}
        user={{ _id: internalId }} // Set the user ID to represent the current user (e.g., ID 1)
        renderComposer={CustomComposer}
        inverted={true} // Set the inverted prop to true to display the chat messages in reverse order
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
