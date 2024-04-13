// ChatBubble.tsx

import React from 'react';
import {View, Text} from 'react-native';
import {ChatBubbleProps, ChatSender} from 'src/types';

function ChatBubble(props: ChatBubbleProps) {
  const sender = props.sender;
  const message = props.message;

  return (
    <View
      style={{
        alignItems: props.sender == ChatSender.User ? 'flex-end' : 'flex-start',
      }}>
      <Text>
        {props.sender}: {message}
      </Text>
    </View>
  );
}

export default ChatBubble;
