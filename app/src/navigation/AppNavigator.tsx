// AppNavigator.tsx

// AppNavigator.tsx

import React from 'react';
import {createDrawerNavigator} from '@react-navigation/drawer';
import Chat from '@screens/Home/Chat';
import {useAppSelector} from '@providers/ChatStore';

const Drawer = createDrawerNavigator();

const AppNavigator = () => {
  const conversations = useAppSelector(
    state => state.conversation.conversations,
  );

  const chatIds = Object.keys(conversations);

  return (
    <Drawer.Navigator initialRouteName="Home">
      <Drawer.Screen
        name="Chat"
        component={Chat}
        initialParams={{chatId: chatIds[0] || null}}
        options={{headerShown: true, drawerLabel: 'Chat', headerTitle: ''}}
      />
    </Drawer.Navigator>
  );
};

export default AppNavigator;
