import Home from './pages/home'
import {Route, BrowserRouter, Routes} from 'react-router-dom';
import ToggleColorMode from "./components/ToggleColorMode.tsx";
import Explore from "./pages/explore.tsx";
import Server from "./pages/server.tsx";
import Login from "./pages/login.tsx";
import {AuthServiceProvider} from "./context/AuthContext.tsx";
import TestLogin from "./pages/testLogin.tsx";
import ProtectedRoute from "./services/ProtectedRoute.tsx";
import Register from "./pages/register.tsx";
import {MembershipProvider} from "./context/MemberContext.tsx";
import MembershipCheck from "./components/Membership/MembershipCheck.tsx";

const App = () => {
    return (
        <BrowserRouter>
            <AuthServiceProvider>
                <ToggleColorMode>
                    <Routes>
                        <Route path="/" element={<Home/>}/>
                        <Route path="/server/:serverId?/:channelId?" element={
                            <ProtectedRoute>
                                <MembershipProvider>
                                    <MembershipCheck>
                                        <Server/>
                                    </MembershipCheck>
                                </MembershipProvider>
                            </ProtectedRoute>
                        }/>
                        <Route path="/explore/:categoryName" element={<Explore/>}/>
                        <Route path='/login' element={<Login/>}/>
                        <Route path="/register" element={<Register/>}/>
                        <Route
                            path="/testlogin"
                            element={
                                <ProtectedRoute>
                                    <TestLogin/>
                                </ProtectedRoute>
                            }
                        />
                    </Routes>
                </ToggleColorMode>
            </AuthServiceProvider>
        </BrowserRouter>
    );
}
export default App
