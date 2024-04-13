// ChatWindow.tsx

import React, {useState, useMemo} from 'react';
import {useDispatch, useSelector} from 'react-redux';
import {ChatBubbleProps, ChatSender, ChatWindowProps} from 'src/types';
import ChatBubble from '@features/Chat/ChatBubble';
import {View, TextInput, Button, StyleSheet} from 'react-native';
import {addMessage, makeSelectChatById} from '@features/Chat/ChatSlice';
import {RootState} from '@providers/ChatStore';

/**
 * TODO:
 *  - Implement a chat window that allows the user to send messages
 *  - The chat window should display the messages sent by the user and the bot
 *  - Implement Redux to manage the state of the chat messages
 *
 *  Currently Only Supports one Chat Store
 */

const ChatWindow: React.FC<ChatWindowProps> = ({chatId}) => {
  const [input, setInput] = useState('');
  const dispatch = useDispatch();

  const selectChatById = useMemo(makeSelectChatById, []);
  const messages =
    useSelector((state: RootState) => selectChatById(state)(chatId)) || [];

  const handleSend = () => {
    dispatch(
      addMessage({chatId, message: {message: input, sender: ChatSender.User}}),
    );
    setInput('');
  };

  return (
    <View style={styles.container}>
      <View style={styles.chat}>
        {messages.map((msg, index) => (
          <ChatBubble key={index} message={msg.message} sender={msg.sender} />
        ))}
      </View>
      <View style={styles.inputContainer}>
        <TextInput
          value={input}
          onChangeText={setInput}
          placeholder="Type a message"
        />
        <Button title="Send" onPress={handleSend} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'space-between',
  },
  chat: {
    flex: 1,
  },
  inputContainer: {
    marginBottom: 10,
  },
});

export default ChatWindow;
