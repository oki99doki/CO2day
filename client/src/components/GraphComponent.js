import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';

const GraphComponent = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        // fetch('/houses/graph-data')
        fetch('/users')
            .then(response => response.json())
            .then(data => {
                setData(JSON.parse(data));
            });
    }, []);

    return (
        <div>
            {data ? (
                <Plot
                    data={data.data}
                    layout={data.layout}
                />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default GraphComponent;
