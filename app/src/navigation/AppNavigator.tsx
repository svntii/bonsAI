// AppNavigator.tsx

// AppNavigator.tsx

import React from 'react';
import {createDrawerNavigator} from '@react-navigation/drawer';
import Chat from '@screens/Home/Chat';

const Drawer = createDrawerNavigator();

const AppNavigator = () => {
  return (
    <Drawer.Navigator initialRouteName="Home">
      <Drawer.Screen
        name="Home"
        component={Chat}
        options={{headerShown: true, drawerLabel: 'Chat', headerTitle: ''}}
      />
    </Drawer.Navigator>
  );
};

export default AppNavigator;
