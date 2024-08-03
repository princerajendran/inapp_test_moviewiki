import React, { useState } from 'react';
import axios from 'axios';

const SearchMovies = () => {
    const [movies, setMovies] = useState([]);
    const [year, setYear] = useState('');
    const [genre, setGenre] = useState('');
    const [type, setType] = useState('');

    const searchMovies = async () => {
        const token = localStorage.getItem('accessToken'); // Ensure the key matches
        if (token) {
            try {
                const response = await axios.get('http://localhost:8000/api/titles/', {
                    params: { year, genre, type },
                    headers: { Authorization: `Bearer ${token}` }
                });
                setMovies(response.data);
            } catch (error) {
                console.error('Error fetching movies:', error);
                alert('Failed to fetch movies.');
            }
        } else {
            console.error('No access token found.');
            alert('You need to log in first.');
        }
    };

    return (
        <div>
            <h1>Search Movies</h1>
            <input type="text" placeholder="Year" value={year} onChange={e => setYear(e.target.value)} />
            <input type="text" placeholder="Genre" value={genre} onChange={e => setGenre(e.target.value)} />
            <input type="text" placeholder="Type" value={type} onChange={e => setType(e.target.value)} />
            <button onClick={searchMovies}>Search</button>
            <div>
                {movies.map(movie => (
                    <div key={movie.tconst}>
                        <h2>{movie.primary_title}</h2>
                        <p>Year: {movie.start_year}</p>
                        <p>Type: {movie.title_type}</p>
                        <p>Genre: {movie.genres}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default SearchMovies;
