import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { loginUser } from "../api/authApi";
import { useAuth } from "./AuthContext";

function Login() {

    const navigate = useNavigate();

    const { login } = useAuth();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            const response = await loginUser({
                email,
                password,
            });

            login(response.access_token);

            navigate("/user");

        } catch (error) {

            alert("Invalid Credentials" + (error.response?.data?.detail ? `: ${error.response.data.detail}` : ""));
        }
    };

    return (

        <form onSubmit={handleSubmit}>

            <h2>Login</h2>

            <input
                type="email"
                placeholder="Email"
                onChange={(e) => setEmail(e.target.value)}
            />

            <br />

            <input
                type="password"
                placeholder="Password"
                onChange={(e) => setPassword(e.target.value)}
            />

            <br />

            <button>

                Login

            </button>

        </form>
    );
}

export default Login;