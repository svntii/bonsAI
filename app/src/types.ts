

export enum ChatSender {
    User = "User",
    Bot = "Bot",
}

export interface ChatBubbleProps {
    message: string;
    sender: ChatSender;
}

export interface ChatState {
    chats: Record<string, ChatBubbleProps[]>;
}

export interface ChatWindowProps {
    chatId: string;
}

export interface ChatListProps {
    
}
