import Home from './pages/home'
import {createBrowserRouter, createRoutesFromElements, Route, RouterProvider} from 'react-router-dom';
import ToggleColorMode from "./components/ToggleColorMode.tsx";
import Explore from "./pages/explore.tsx";
import Server from "./pages/server.tsx";


const router = createBrowserRouter(
    createRoutesFromElements(
        <Route>
            <Route path="/" element={<Home/>}/>
            <Route path="/server/:serverId?/:channelId?" element={<Server/>}/>
            <Route path="/explore/:categoryName" element={<Explore/>}/>
        </Route>
    )
)

const App = () => {
    return (
        <ToggleColorMode>
            <RouterProvider router={router}/>
        </ToggleColorMode>
    );
}
export default App
