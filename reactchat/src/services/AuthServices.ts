import {AuthServiceProps} from "../@types/auth-service";
import axios from "axios";
import {useState} from "react";
import {BASE_URL} from "../config.ts";
import {useNavigate} from "react-router-dom";


export const useAuthService: AuthServiceProps = () => {

    const navigate = useNavigate();

    const getInitialLoggedInValue = () => {
        const loggedIn = localStorage.getItem("isLoggedIn");
        return loggedIn !== null && loggedIn === "true";
    };

    const [isLoggedIn, setIsLoggedIn] = useState<boolean>((getInitialLoggedInValue))

    const getUserDetails = async () => {
        try {
            const userId = localStorage.getItem("user_id")
            const response = await axios.get(
                `${BASE_URL}/auth/account/?userId=${userId}`,
                {withCredentials: true}
            );
            const userDetails = response.data;
            localStorage.setItem("username", userDetails[0].username);
            setIsLoggedIn(true);
            localStorage.setItem("isLoggedIn", "true")
        } catch (err: any) {
            setIsLoggedIn(false)
            localStorage.setItem("isLoggedIn", "false")
            return err;
        }
    }

    // const getUserIdFromToken = (access: string) => {
    //     const token = access
    //     const tokenParts = token.split('.')
    //     const encodedPayLoad = tokenParts[1]
    //     const decodedPayLoad = atob(encodedPayLoad)
    //     const payLoadData = JSON.parse(decodedPayLoad)
    //     const userId = payLoadData.user_id
    //
    //     return userId
    // }

    const login = async (username: string, password: string) => {
        try {
            const response = await axios.post(
                `${BASE_URL}/auth/token/`, {
                    username,
                    password,
                }, {withCredentials: true}
            );

            const user_id = response.data.user_id;
            localStorage.setItem("isLoggedIn", "true")
            localStorage.setItem('user_id', user_id)
            setIsLoggedIn(true)
            getUserDetails()

        } catch (err: any) {
            return err.response.status;
        }
    }

    const refreshAccessToken = async () => {
        try {
            await axios.post(
                `${BASE_URL}/auth/token/refresh/`, {},
                {withCredentials: true}
            );
        } catch (refreshError) {
            return Promise.reject(refreshError)
        }
    }

    const logout = async () => {
        localStorage.setItem("isLoggedIn", "false");
        localStorage.removeItem("user_id");
        localStorage.removeItem("username");
        setIsLoggedIn(false);
        navigate('/login');

        try {
            await axios.post(
                `${BASE_URL}/auth/logout/`, {},
                {withCredentials: true}
            );
        } catch (refreshError) {
            return Promise.reject(refreshError)
        }

    }

    return {login, isLoggedIn, logout, refreshAccessToken}
}
export default useAuthService;