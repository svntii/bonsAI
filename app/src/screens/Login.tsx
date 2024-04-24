// Home.tsx
import React from 'react';
import {View} from 'react-native';
import LoginHeader from '@features/Login/LoginHeader';
import LoginField from '@features/Login/LoginField';

const Login = (navigation: any) => {
  return (
    <View>
      <LoginHeader />
      <LoginField />
    </View>
  );
};

export default Login;
