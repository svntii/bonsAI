import {IMessage} from 'react-native-gifted-chat';
import type {RouteProp} from '@react-navigation/native';

export enum ChatSender {
  User = 'User',
  Bot = 'Bot',
}

export interface ChatBubbleProps {
  message: string;
  sender: ChatSender;
}

export interface ChatState {
  chats: Record<string, ChatBubbleProps[]>;
}

export interface Conversation {
  id: string;
  messages: IMessage[];
}

export interface ChatWindowProps {
  chatId: string;
}

export interface ChatListProps {}

export type RootStackParamList = {
  Home: undefined;
  Chat: {chatId: string};
  LoggedIn: undefined;
  SignIn: undefined;
};
export type ChatScreenRouteProp = RouteProp<RootStackParamList, 'Chat'>;
