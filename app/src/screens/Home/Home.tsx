import React from 'react';
import { View, Text, Button } from 'react-native';

const LandingPage = ({ navigation }: { navigation: any }) => {
  const handleChatButtonPress = () => {
    navigation.navigate('Chat', { screen: 'Chat' });
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Welcome to our app!</Text>
      <Button title="Start Chatting" onPress={handleChatButtonPress} />
    </View>
  );
};

export default LandingPage;
