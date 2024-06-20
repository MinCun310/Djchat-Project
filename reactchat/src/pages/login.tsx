import {useFormik} from 'formik';
import {useNavigate} from "react-router-dom";
import {useAuthServiceContext} from "../context/AuthContext.tsx";

const Login = () => {
    const {login} = useAuthServiceContext()
    const navigate = useNavigate();
    const formik = useFormik({
        initialValues: {
            username: '',
            password: '',
        },
        onSubmit: async (values) => {
            const { username, password } = values;
            const res = await login(username, password);
            if (res){
                console.log('==========', res);
            }else {
                navigate('/testlogin');
            }
        }
    })
    return <div>
        <h1>Login</h1>
        <form onSubmit={formik.handleSubmit}>
            <label htmlFor="username">Username</label>
            <input
                type="text"
                name="username"
                id="username"
                onChange={formik.handleChange}
                value={formik.values.username}
            />
            <label htmlFor="password">Password</label>
            <input
                type="password"
                name="password"
                id="password"
                onChange={formik.handleChange}
                value={formik.values.password}
            />
            <button type="submit">Login</button>
            <button onClick={() => navigate('/register')}>Register</button>
        </form>
    </div>
}
export default Login;