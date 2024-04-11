// Home.tsx
import React from 'react';
import { View } from 'react-native';
import BonsaiStyles from "@theme/BonsaiStyles"
import LoginHeader from '@features/Login/LoginHeader';
import LoginField from '@features/Login/LoginField';

const Login = () => {
    return(
        <View style={BonsaiStyles.container}>
            <LoginHeader />
            <LoginField />
        </View>
    );

};

export default Login;