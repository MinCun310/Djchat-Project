import Home from './pages/home'
import {createBrowserRouter, createRoutesFromElements, Route, RouterProvider} from 'react-router-dom';
import ToggleColorMode from "./components/ToggleColorMode.tsx";
import Explore from "./pages/explore.tsx";
import Server from "./pages/server.tsx";
import Login from "./pages/login.tsx";
import {AuthServiceProvider} from "./context/AuthContext.tsx";
import TestLogin from "./pages/testLogin.tsx";
import ProtectedRoute from "./services/ProtectedRoute.tsx";


const router = createBrowserRouter(
    createRoutesFromElements(
        <Route>
            <Route path="/" element={<Home/>}/>
            <Route path="/server/:serverId?/:channelId?" element={<Server/>}/>
            <Route path="/explore/:categoryName" element={<Explore/>}/>
            <Route path='/login' element={<Login/>}/>
            <Route
                path="/testlogin"
                element={
                    <ProtectedRoute>
                        <TestLogin/>
                    </ProtectedRoute>
                }
            />
        </Route>
    )
)

const App = () => {
    return (
        <AuthServiceProvider>
            <ToggleColorMode>
                <RouterProvider router={router}/>
            </ToggleColorMode>
        </AuthServiceProvider>
    );
}
export default App
