import { configureStore } from '@reduxjs/toolkit';
import ChatSlice from '@features/Chat/ChatSlice';


export const ChatStore = configureStore({
    reducer: {
      chat: ChatSlice,
    },
  });


export type RootState = ReturnType<typeof ChatStore.getState>;
export type AppDispatch = typeof ChatStore.dispatch;