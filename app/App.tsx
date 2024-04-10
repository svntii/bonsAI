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
import Login from "@screens/Login";


function App(): React.JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';

  const backgroundStyle = {
    flex: 1,
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  return (
    <SafeAreaView style={backgroundStyle}>
      <Login />
    </SafeAreaView>
  );
}

export default () => {
  return (
    <ThemeProvider>
      <App />
    </ThemeProvider>
  );
}
