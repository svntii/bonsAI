import React, { useEffect } from 'react';
import { View, StyleSheet, Button, TextInput, Text, TouchableOpacity, Image } from 'react-native';
import { GiftedChat, IMessage, Composer, InputToolbar, Send, Bubble } from 'react-native-gifted-chat';
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
  
  const renderInputToolbar = (props) => {
    return (

      <View style={{flex:1}}>
        <InputToolbar {...props} containerStyle={styles.inputToolbar}>
        </InputToolbar>
      </View>
    );
  }

  const renderSend = (props) => {
    return (
      <TouchableOpacity>
      <Send {...props} >
        <Image source={require('../../assets/send.png')} style={styles.sendImage} />
      </Send>
      </TouchableOpacity>

    );
  }

  const renderSuggestions = (props) => {
    return (
      <View style={{ flexDirection: 'row', justifyContent: 'space-around', padding: 5 }}>
      {/* Touchable components */}
      <TouchableOpacity
        style={styles.responseButton}
        onPress={() => handleSendResponse('Yes', internalId)}
      >
        <Text style={styles.responseButtonText}>Yes</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={styles.responseButton}
        onPress={() => handleSendResponse('No', internalId)}
      >
        <Text style={styles.responseButtonText}>No</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={styles.responseButton}
        onPress={() => handleSendResponse('Maybe', internalId)}
      >
        <Text style={styles.responseButtonText}>Maybe</Text>
      </TouchableOpacity>
    </View>
    );
  }
  
  const renderComposer = (props) => {
    return (
      
    <View style={{ flex: 1 }}>
      {renderSuggestions(props)}
      <Composer
        {...props}
      />
    </View>
      
    );
  };

  const renderChatFooter = () => {
    return(
      <View style={{height:80}}></View>
    )
  }

  const renderBubble = (props) => {
    return (
      <Bubble {...props}
      textStyle={ styles.bubbleTextStyle }
      wrapperStyle={ styles.bubbleWrapperStyle }
      />
  );
  }

  const renderAvatar = (props) => {
    return (
      <Image source={require('../../assets/stewieAvatar.png')} style={styles.avatarImage}/>
    )
  }


  return (
    <View style={styles.container}>
      <GiftedChat
        messages={currentConversation.messages}
        onSend={onSend}
        user={{ _id: internalId }} // Set the user ID to represent the current user (e.g., ID 1)
        renderInputToolbar={renderInputToolbar} // Use CustomInputToolbar
        renderComposer={renderComposer} // Use CustomInputToolbar
        renderSend={renderSend}
        renderBubble={renderBubble}
        alwaysShowSend={true}
        renderChatFooter={renderChatFooter}
        renderAvatar={renderAvatar}
        renderAvatarOnTop={true}
        />
    </View>
  );
}
const primaryColor = '#05490F';
const secondaryColor = '#121F33';
const red = '#C62828';
const white = "#FFFFFF";
const black = "#030C1A";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: black
  },
  responseButtonText: { 
    color: white
  },
  responseButton: {
    backgroundColor: primaryColor,
    padding: 15,
    borderRadius: 20,
    margin: 5,
  },

  inputToolbar: {
    marginLeft: 5,
    marginRight: 5,
    marginBottom: 5,
    marginTop: 5,
    borderWidth: 0,
    borderRadius: 20,
    backgroundColor: white,
  },
  sendImage: {
    width: 30,
    height: 30,
    margin: 10,
  },
  bubbleTextStyle: {
    left: {
      color: 'white',
      fontFamily: "Roboto"
    },
    right: {
      color: 'white',
      fontFamily: "Roboto"
    }
  },
  bubbleWrapperStyle: {
    left: {
      backgroundColor: secondaryColor,
      color: white,
    },
    right: {
      backgroundColor: primaryColor,
      color: white
    }
    },
  composerStyle: {
    flex: 1,
  },
  avatarImage: {
    width: 30, 
    height: 30,
    borderRadius: 15,
  },
  
});
