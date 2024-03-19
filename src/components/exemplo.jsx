import React from 'react';
import styles from '../styles/components/exemplo.module.css';

export default function Exemplo() {
	return (
		<div className={styles.container}>
			{/* utilizando multiplas classes com módulo css */}
			<div className={`${styles.item} ${styles.item1}`}>
				Item 1
			</div>
			<div className={`${styles.item} ${styles.item2}`}>
				Item 2
			</div>
			<div className={`${styles.item} ${styles.item3}`}>
				Item 3
			</div>
		</div>
	)
}