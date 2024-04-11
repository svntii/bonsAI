// ChatList.tsx

import React from "react";
import { View, Text, StyleSheet } from "react-native";
import { useSelector } from "react-redux";
import { ChatListProps } from "src/types";
import { selectChats } from "@features/Chat/ChatSlice";

const ChatList: React.FC<ChatListProps> = () => {
    
    const chats = useSelector(selectChats)

    const handleChatClick = (chatId: string) => {
        console.log(`Chat ${chatId} clicked`);
    }
    
    return (
        <View>
            <Text>All Chats</Text>
        </View>
    );
}