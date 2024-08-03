import React, { useState } from 'react';
import axios from 'axios';
import './SearchMovies.css';

const SearchMovies = () => {
    const [movies, setMovies] = useState([]);
    const [year, setYear] = useState('');
    const [genre, setGenre] = useState('');
    const [type, setType] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const searchMovies = async () => {
        const token = localStorage.getItem('accessToken');
        if (token) {
            setLoading(true);
            setError('');
            try {
                const response = await axios.get('http://localhost:8000/api/titles/', {
                    params: { year, genre, type },
                    headers: { Authorization: `Bearer ${token}` }
                });
                setMovies(response.data);
            } catch (error) {
                console.error('Error fetching movies:', error);
                setError('Failed to fetch movies.');
            } finally {
                setLoading(false);
            }
        } else {
            console.error('No access token found.');
            alert('You need to log in first.');
        }
    };

    return (
        <div className="search-movies-container">
            <h1>Search Movies</h1>
            {error && <p className="error-message">{error}</p>}
            <div className="search-form">
                <input
                    type="text"
                    placeholder="Year"
                    value={year}
                    onChange={(e) => setYear(e.target.value)}
                    className="search-input"
                />
                <input
                    type="text"
                    placeholder="Genre"
                    value={genre}
                    onChange={(e) => setGenre(e.target.value)}
                    className="search-input"
                />
                <input
                    type="text"
                    placeholder="Type"
                    value={type}
                    onChange={(e) => setType(e.target.value)}
                    className="search-input"
                />
                <button onClick={searchMovies} className="search-button" disabled={loading}>
                    {loading ? 'Searching...' : 'Search'}
                </button>
            </div>
            <div className="movies-grid">
                {movies.length === 0 ? (
                    <p>No movies found.</p>
                ) : (
                    movies.map(movie => (
                        <div key={movie.tconst} className="movie-card">
                            <h2>{movie.primary_title}</h2>
                            <p>Year: {movie.start_year}</p>
                            <p>Type: {movie.title_type}</p>
                            <p>Genre: {movie.genres}</p>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default SearchMovies;
