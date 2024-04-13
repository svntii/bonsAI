// AppNavigator.tsx

// AppNavigator.tsx

import React from 'react';
import {createDrawerNavigator} from '@react-navigation/drawer';
import Home from '@screens/Home/Home';

const Drawer = createDrawerNavigator();

const AppNavigator = () => {
  return (
    <Drawer.Navigator initialRouteName="Home">
      <Drawer.Screen
        name="Home"
        component={Home}
        options={{headerShown: true, drawerLabel: 'Home', headerTitle: ''}}
      />
    </Drawer.Navigator>
  );
};

export default AppNavigator;
