import React from 'react';

const Schedule: React.FC = () => {
    const competitions = [
        { date: '2023-10-15', time: '10:00 AM', location: 'School Gymnasium' },
        { date: '2023-11-05', time: '1:00 PM', location: 'Community Center' },
        { date: '2023-12-01', time: '9:00 AM', location: 'City Stadium' },
    ];

    return (
        <div>
            <h1>Competition Schedule</h1>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Time</th>
                        <th>Location</th>
                    </tr>
                </thead>
                <tbody>
                    {competitions.map((competition, index) => (
                        <tr key={index}>
                            <td>{competition.date}</td>
                            <td>{competition.time}</td>
                            <td>{competition.location}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Schedule;