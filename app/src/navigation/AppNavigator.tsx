import React from 'react';
import {createStackNavigator} from '@react-navigation/stack';
import Home from '@screens/Home/Home';
import Chat from '@screens/Home/Chat';
import {useAppSelector} from '@providers/ChatStore';

const Stack = createStackNavigator();

const AppNavigator = () => {
  const conversations = useAppSelector(
    state => state.conversation.conversations,
  );
  const chatIds = Object.keys(conversations);

  return (
    <Stack.Navigator initialRouteName="Home">
      <Stack.Screen
        name="Home"
        component={Home}
        options={{title: '', headerShown: false}}
      />
      <Stack.Screen
        name="Chat"
        component={Chat}
        options={{title: '', headerShown: false, headerLeft: null}}
      />
    </Stack.Navigator>
  );
};

export default AppNavigator;
