// LoginField.tsx
import React, { useState } from 'react';
import { TextInput, Button, View } from 'react-native';
import BonsaiStyles from "@theme/BonsaiStyles"


const LoginField = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    // Handle login logic
    console.log(`Email: ${email}, Password: ${password}`);
  };

  return (
    <View>
      <TextInput
        style={BonsaiStyles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        style={BonsaiStyles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <Button
        title="Login"
        onPress={handleLogin}
      />
    </View>
  );
};

export default LoginField;