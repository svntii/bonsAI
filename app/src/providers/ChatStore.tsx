import {configureStore} from '@reduxjs/toolkit';
export const ChatStore = configureStore({
  reducer: {},
});

export type RootState = ReturnType<typeof ChatStore.getState>;
export type AppDispatch = typeof ChatStore.dispatch;
