import {createSlice, PayloadAction} from '@reduxjs/toolkit';
import {Conversation} from '@T/types';
import {IMessage} from 'react-native-gifted-chat';

interface ConversationState {
  conversations: Record<string, Conversation>;
  currentConversation: Conversation | null;
}

const initialState: ConversationState = {
  conversations: {},
  currentConversation: null,
};

// Action Payloads
interface AddConversationPayload {
  id: string;
  conversation: Conversation;
}

interface AddMessagePayload {
  conversationId: string;
  message: IMessage; // TODO
}

interface GetConversationPayload {
  id: string;
}

const ConversationSlice = createSlice({
  name: 'conversation',
  initialState,
  reducers: {
    addConversation: (state, action: PayloadAction<AddConversationPayload>) => {
      return {
        ...state,
        conversations: {
          ...state.conversations,
          [action.payload.id]: action.payload.conversation,
        },
      };
    },
    addMessage: (state, action: PayloadAction<AddMessagePayload>) => {
      const conversation = state.conversations[action.payload.conversationId];
      return {
        ...state,
        conversations: {
          ...state.conversations,
          [action.payload.conversationId]: {
            ...conversation,
            messages: [...conversation.messages, action.payload.message],
          },
        },
      };
    },
    getConversation: (state, action: PayloadAction<GetConversationPayload>) => {
      return {
        ...state,
        currentConversation: state.conversations[action.payload.id],
      };
    },
  },
});

export const {addConversation, addMessage, getConversation} =
  ConversationSlice.actions;

export default ConversationSlice;
