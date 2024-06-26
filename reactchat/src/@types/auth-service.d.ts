export interface AuthServiceProps {
    login: (username: string, password: string) => Promise<void>;
    isLoggedIn: boolean;
    logout: () => Promise<void>;
    refreshAccessToken: () => Promise<void>;
}