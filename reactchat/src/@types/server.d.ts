export interface Server {
    id: number;
    name: string;
    description: string;
    icon: string;
    category: string;
    channel_server: {
        id: number;
        name: string;
        server: number;
        topic: string;
        owner: number;
    }[];
}