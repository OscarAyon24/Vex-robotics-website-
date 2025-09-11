import React from 'react';

import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import AboutMe from './components/AboutMe';
import Teams from './components/Teams';
import Schedule from './components/Schedule';


const App: React.FC = () => {
    return (
        <Router>
            <div>
                <nav style={{ marginBottom: '20px' }}>
                    <Link to="/about" style={{ marginRight: '10px' }}>About</Link>
                    <Link to="/teams" style={{ marginRight: '10px' }}>Teams</Link>
                    <Link to="/schedule">Schedule</Link>
                </nav>
                <Routes>
                    <Route path="/about" element={<AboutMe />} />
                    <Route path="/teams" element={<Teams />} />
                    <Route path="/schedule" element={<Schedule />} />
                    <Route path="*" element={<AboutMe />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;