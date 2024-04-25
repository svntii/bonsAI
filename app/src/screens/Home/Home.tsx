import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';

const LandingPage = ({ navigation }: { navigation: any }) => {
  const handleChatButtonPress = () => {
    navigation.navigate('Chat', { screen: 'Chat' });
  };

  const renderTitle = () => {
    return (
      <View style={styles.titleContainer}>
        <Text style={styles.title}>Stewie</Text>
        <Text style={styles.botName}>theStedsBot</Text>
      </View>
    );
  };

  const renderSubtitle = () => {
    return (
      <View style={styles.subtitleContainer}>
        <Text style={styles.subtitle}>Your dorm's friendly toilet ghost</Text>
      </View>
    );
  };

  const renderButton = () => {
    return (
      <TouchableOpacity style={styles.buttonContainer} onPress={handleChatButtonPress}>
        <Text style={styles.buttonText}>Get Started</Text>
      </TouchableOpacity>
    );
  };

  return (
    <View style={styles.container}>
      {renderTitle()}
      {renderSubtitle()}
      {renderButton()}
    </View>
  );
};

const primaryColor = '#05490F';
const secondaryColor = '#121F33';
const red = '#C62828';
const white = "#FFFFFF";
const black = "#030C1A";
const font = "Roboto";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  titleContainer: {
    alignItems: 'center',
  },
  title: {
    fontFamily: font,
    fontSize: 80, // Increased font size for the title
    fontWeight: 'bold',
  },
  botName: {
    fontFamily: 'Roboto',
    fontSize: 40,
    color: '#888',
  },
  subtitleContainer: {
    marginBottom: 20,
  },
  subtitle: {
    fontFamily: 'Roboto',
    fontSize: 15,
    textAlign: 'center',
  },
  buttonContainer: {
    width: '100%',
    backgroundColor: primaryColor,
    borderRadius: 15,
    paddingVertical: 12,
    paddingHorizontal: 16,
    marginTop: 20,
  },
  
  buttonText: {
    fontFamily: 'Roboto',
    fontSize: 18,
    color: 'white', // Button text color set to white
    textAlign: 'center',
  },
});

export default LandingPage;
