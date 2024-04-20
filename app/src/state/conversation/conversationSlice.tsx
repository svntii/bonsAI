import {createSlice, PayloadAction} from '@reduxjs/toolkit';
import {Conversation} from '@T/types';
import {IMessage, User} from 'react-native-gifted-chat';

interface ConversationState {
  conversations: Record<string, Conversation>;
  currentConversation: Conversation;
}

const initialState: ConversationState = {
  currentConversation: {id: '0', messages: []},
  conversations: {current: {id: '0', messages: []}},
};

// Action Payloads
interface AddConversationPayload {
  id: string;
  conversation: Conversation;
}

interface AddMessagePayload {
  conversationId: string;
  message: IMessage;
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
      if (conversation) {
        return {
          ...state,
          conversations: {
            ...state.conversations,
            [action.payload.conversationId]: {
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
            [action.payload.conversationId]: {
              id: action.payload.conversationId,
              messages: [action.payload.message],
            },
          },
        };
      }
    },
    getConversation: (state, action: PayloadAction<GetConversationPayload>) => {
      if (!state.conversations[action.payload.id]) {
        return {
          ...state,
          conversations: {
            ...state.conversations,
            [action.payload.id]: {
              id: action.payload.id,
              messages: [],
            },
          },
        };
      } else {
        return {
          ...state,
          currentConversation: state.conversations[action.payload.id],
        };
      }
    },
  },
});

export const {addConversation, addMessage, getConversation} =
  ConversationSlice.actions;

export default ConversationSlice;
