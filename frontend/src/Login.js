import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Login.css'; // Import the CSS file for styling

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const login = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/token/', {
                username: username,
                password: password
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            localStorage.setItem('accessToken', response.data.access);
            localStorage.setItem('refreshToken', response.data.refresh);
            navigate('/search-movies');
        } catch (error) {
            console.error('Login failed:', error);
            if (error.response && error.response.data) {
                setError('Login failed. Please check your credentials.');
            } else {
                setError('An error occurred. Please try again.');
            }
        }
    };

    return (
        <div className="login-container">
            <h1>Login</h1>
            {error && <p className="error-message">{error}</p>}
            <div className="login-form">
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    className="login-input"
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="login-input"
                />
                <button onClick={login} className="login-button">Login</button>
            </div>
        </div>
    );
};

export default Login;
