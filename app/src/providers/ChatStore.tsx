import {configureStore} from '@reduxjs/toolkit';
import ConversationSlice from '../state/conversation/conversationSlice';
import {useDispatch, useSelector} from 'react-redux';

export const ChatStore = configureStore({
  reducer: {
    conversation: ConversationSlice.reducer,
  },
});

export type RootState = ReturnType<typeof ChatStore.getState>;
export type AppDispatch = typeof ChatStore.dispatch;
export const useAppDispatch = useDispatch.withTypes<AppDispatch>();
export const useAppSelector = useSelector.withTypes<RootState>();
