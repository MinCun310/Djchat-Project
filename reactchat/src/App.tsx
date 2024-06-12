import Home from './pages/home'
import {createBrowserRouter, createRoutesFromElements, Route, RouterProvider} from 'react-router-dom';
import {ThemeProvider} from "@mui/material";
import {createMuiTheme} from './themes/theme'
import ToggleColorMode from "./components/ToggleColorMode.tsx";

const router = createBrowserRouter(
    createRoutesFromElements(
        <Route>
            <Route path="/home" element={<Home/>}/>
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
