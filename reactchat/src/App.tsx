import Home from './pages/home'
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom';
import {ThemeProvider} from "@mui/material";
import { createMuiTheme} from './themes/theme'

const router = createBrowserRouter(
    createRoutesFromElements(
        <Route>
          <Route path="/home" element={<Home />} />
        </Route>
    )
)

const App = () => {
    const theme = createMuiTheme();
    return (
        <ThemeProvider theme={theme}>
            <RouterProvider router={router} />
        </ThemeProvider>
    );
}
export default App
