import React, { useState } from "react";
import api from "../services/api";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        try {
            const response = await api.post("/auth/login", { email, password });
            localStorage.setItem("token", response.data.token);
            window.location.href = "/dashboard";
        } catch (error) {
            alert("Invalid credentials");
        }
    };

    return (
        <div className="w-96 p-6 bg-white rounded-xl shadow-md">
            <h2 className="text-2xl font-bold mb-4">Login</h2>
            <input className="w-full p-2 border mb-3" type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
            <input className="w-full p-2 border mb-3" type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
            <button className="w-full bg-blue-500 text-white p-2 rounded-lg" onClick={handleLogin}>Login</button>
        </div>
    );
};
export default Login;
