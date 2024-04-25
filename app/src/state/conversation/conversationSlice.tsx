import {createSlice, PayloadAction} from '@reduxjs/toolkit';
import {Conversation} from '@T/types';
import {IMessage, User} from 'react-native-gifted-chat';

interface ConversationState {
  conversations: Record<string, Conversation>;
  currentConversation: Conversation;
}
// id '0' is reserved for the bot
const initialState: ConversationState = {
  currentConversation: {internalId: '1', backendId: '', messages: []},
  conversations: {1: {internalId: '1', backendId: '', messages: []}},
};

// Action Payloads
interface AddConversationPayload {
  internalId: string;
  conversation: Conversation;
}

interface AddMessagePayload {
  internalId: string;
  message: IMessage;
}
interface GetConversationPayload {
  internalId: string;
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
          [action.payload.internalId]: action.payload.conversation,
        },
      };
    },
    addMessage: (state, action: PayloadAction<AddMessagePayload>) => {
      const conversation = state.conversations[action.payload.internalId];
      if (conversation) {
        return {
          ...state,
          conversations: {
            ...state.conversations,
            [action.payload.internalId]: {
              ...conversation,
              messages: [action.payload.message, ...conversation.messages],
            },
          },
        };
      } else {
        return {
          ...state,
          conversations: {
            ...state.conversations,
            [action.payload.internalId]: {
              internalId: action.payload.internalId,
              messages: [action.payload.message],
            },
          },
        };
      }
    },
    getConversation: (state, action: PayloadAction<GetConversationPayload>) => {
      if (!state.conversations[action.payload.internalId]) {
        return {
          ...state,
          conversations: {
            ...state.conversations,
            [action.payload.internalId]: {
              internalId: action.payload.internalId,
              messages: [],
            },
          },
        };
      } else {
        return {
          ...state,
          currentConversation: state.conversations[action.payload.internalId],
        };
      }
    },
  },
});

export const {addConversation, addMessage, getConversation} =
  ConversationSlice.actions;

export default ConversationSlice;
