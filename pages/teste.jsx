// import TesteComponent from "@/components/testeComponent"
import styles from '../src/styles/pages/teste.module.css';
import dynamic from 'next/dynamic';

import TesteComponent from '@/components/testeComponent';

// const TesteComponent = dynamic(
// 	() =>
// 		import(
// 			'@/components/testeComponent'
// 		),
// 	{
// 		ssr: false,
// 		loading: () => <>Loading...</>,
// 	},
// );

export default function Teste() {
	return (
		<div className={styles.mainContent}>
			<TesteComponent />
		</div>
	)
}