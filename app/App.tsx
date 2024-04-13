/**
 * React Native App
 * 
 *
 * @format
 */

import React from 'react';
import {
  SafeAreaView,
  useColorScheme,
} from 'react-native';

import {
  Colors,
} from 'react-native/Libraries/NewAppScreen';

// Back4App
import AsyncStorage from '@react-native-async-storage/async-storage';
import Parse from 'parse/react-native';
Parse.setAsyncStorage(AsyncStorage);

// Imports
import { ThemeProvider } from '@providers/ThemeContext';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
const Drawer = createDrawerNavigator();



import { Provider } from 'react-redux';
import { ChatStore } from '@providers/ChatStore';
import Header from '@features/Header/Header';
import Login from '@screens/Login';


function App(): React.JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';

  const backgroundStyle = {
    flex: 1,
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  return (
    <SafeAreaView style={backgroundStyle}>
      <NavigationContainer>
        <Drawer.Navigator initialRouteName='Login'>
          <Drawer.Screen name='Login' component={Login} />
        </Drawer.Navigator>
      </NavigationContainer>
    </SafeAreaView>
  );
}

export default () => {
  return (
    <ThemeProvider>
      <Provider store={ChatStore}>
        <App />
      </Provider>
    </ThemeProvider>
  );
}
