import {createSlice, PayloadAction} from '@reduxjs/toolkit';
import {Conversation} from '@T/types';
import {IMessage} from 'react-native-gifted-chat';

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

interface UpdateConversationPayload {
  internalId: string;
  newBackendId: string;
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
    updateConversation: (
      state,
      action: PayloadAction<UpdateConversationPayload>,
    ) => {
      const conversation = state.conversations[action.payload.internalId];
      if (conversation) {
        // conversation found
        return {
          ...state,
          conversations: {
            ...state.conversations,
            [action.payload.internalId]: {
              ...conversation,
              backendId: action.payload.newBackendId,
            },
          },
        };
      } else {
        // No conversation found
        return state;
      }
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
        return state;
      }
    },
    getConversation: (state, action: PayloadAction<GetConversationPayload>) => {
      return {
        ...state,
        currentConversation: state.conversations[action.payload.internalId],
      };
    },
  },
});

export const {
  addConversation,
  addMessage,
  getConversation,
  updateConversation,
} = ConversationSlice.actions;

export default ConversationSlice;