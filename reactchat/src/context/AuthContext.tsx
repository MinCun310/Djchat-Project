import React, {createContext, useContext} from 'react';
import {AuthServiceProps} from '../@types/auth-service';
import {useAuthService} from '../services/AuthServices.ts';


const AuthServiceContext = createContext<AuthServiceProps | null>(null);

export function AuthServiceProvider(props: React.PropsWithChildren<{}>) {
    const authService = useAuthService();
    return (
        <AuthServiceContext.Provider value={authService}>
            {props.children}
        </AuthServiceContext.Provider>
    )
}
export function useAuthServiceContext():AuthServiceProps{
    const context = useContext(AuthServiceContext);

    if(context===null){
        throw new Error('Error - You have to used the AuthServiceProvider')
    }
    return context;
}