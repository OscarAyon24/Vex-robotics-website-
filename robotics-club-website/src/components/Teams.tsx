import React from 'react';

const Teams: React.FC = () => {
    const teams = [
        {
            name: 'Design Team',
            description: 'Responsible for creating the robot design and aesthetics.'
        },
        {
            name: 'Programming Team',
            description: 'Focuses on coding and software development for the robot.'
        },
        {
            name: 'Build Team',
            description: 'Handles the assembly and construction of the robot.'
        },
        {
            name: 'Marketing Team',
            description: 'Promotes the robotics club and manages outreach activities.'
        }
    ];

    return (
        <div>
            <h1>Teams</h1>
            <ul>
                {teams.map((team, index) => (
                    <li key={index}>
                        <h2>{team.name}</h2>
                        <p>{team.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Teams;