// ChatSlice.ts

import {ChatBubbleProps, ChatState} from 'src/types';
import {createSlice, PayloadAction} from '@reduxjs/toolkit';
import {createSelector} from 'reselect';
import {RootState} from '@providers/ChatStore';

const initialState: ChatState = {
  chats: {},
};

export const ChatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    addMessage: (
      state,
      action: PayloadAction<{chatId: string; message: ChatBubbleProps}>,
    ) => {
      const {chatId, message} = action.payload;
      if (!state.chats[chatId]) {
        state.chats[chatId] = [];
      }
      state.chats[chatId].push(message);
    },
    startChat: (state, action: PayloadAction<{chatId: string}>) => {
      const chatId = action.payload.chatId;
      if (!state.chats[chatId]) {
        state.chats[chatId] = [];
      }
    },
  },
});

export const {addMessage} = ChatSlice.actions;

// Selectors
export const selectChats = (state: RootState) => state.chat.chats;

export const makeSelectChatById = () =>
  createSelector([selectChats], chats => (chatId: string) => chats[chatId]);

export default ChatSlice.reducer;
