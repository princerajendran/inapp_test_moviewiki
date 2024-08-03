import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const login = async () => {
        try {
            // Send login request
            const response = await axios.post('http://127.0.0.1:8000/token/', {
                username: username,
                password: password
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
    
            // Set tokens in local storage
            localStorage.setItem('accessToken', response.data.access);
            localStorage.setItem('refreshToken', response.data.refresh);
    
            // Redirect to search movies page
            navigate('/search-movies');
        } catch (error) {
            console.error('Login failed:', error);
            if (error.response && error.response.data) {
                console.error('Error details:', error.response.data);
            }
            alert('Login failed. Please check your credentials.');
        }
    };
    
    return (
        <div>
            <h1>Login</h1>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={login}>Login</button>
        </div>
    );
};

export default Login;
