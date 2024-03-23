import { useEffect, useState } from 'react';

import dynamic from 'next/dynamic';
import axios from 'axios'

const Plot = dynamic(
	() =>
		import(
			'react-plotly.js'
		),
	{
		ssr: false,
		loading: () => <>Loading...</>,
	},
);

export default function TesteComponent() {
	const [dadosGrafico, setDadosGrafico] = useState(null)

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await axios.get('api/teste');
				const data = response.data
				setDadosGrafico([{
					x: Object.values(data.Species),
					y: Object.values(data.PetalLengthCm),
					type: 'bar'
				}]);
			} catch (error) {
				console.error('Error fetching data:', error);
			}
		};

		fetchData();
	}, []);

	return (
		<Plot data={dadosGrafico} layout={{
			title: "Petal length for every species",
			xaxis: {
				title: "Species"
			},
			yaxis: {
				title: "Petal Length (cm)"
			},
		}} />
	)
}