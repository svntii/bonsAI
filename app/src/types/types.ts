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
  internalId: string;
  backendId: string;
  messages: IMessage[];
}

export interface BonsaAIChat {
  messages: IMessage[];
  sources: string[];
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
