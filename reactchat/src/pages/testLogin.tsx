import {useAuthServiceContext} from "../context/AuthContext.tsx";
import {useState} from "react";
import axios from "axios";
import useAxiosWithInterceptor from "../helpers/jwtinterceptor.tsx";

const TestLogin = () => {
    const {isLoggedIn, logout} = useAuthServiceContext();
    const [username, setUsername] = useState('');
    const jwtAxios = useAxiosWithInterceptor();

    const getUserDetails = async () => {
        try {
            const userId = localStorage.getItem("userId")
            const accessToken = localStorage.getItem("access_token")
            const response = await jwtAxios.get(
                `http://127.0.0.1:8000/api/auth/account/?userId=${userId}`, {
                    headers: {
                        Authorization: `Bearer ${accessToken}`
                    }
                });
            const userDetails = response.data;
            setUsername(userDetails[0].username);
        } catch (err: any) {
            return err;
        }
    }

    return (
        <>
            <div>{isLoggedIn.toString()}</div>
            <div>
                <button onClick={logout}>Logout</button>
                <button onClick={getUserDetails}>Get User Details</button>
            </div>
            <div>Username: {username}</div>
        </>
    );
};
export default TestLogin;
