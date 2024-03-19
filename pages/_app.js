import Head from "next/head"


import "../src/styles/global.css"


export default function App({ Component, pageProps }) {
    return (
        <>
            <Head>
                <title>Cafe com Leide</title>

                {/*SEO(search engine otimization)*/}
                <meta name="description" content="" />{/*Descrição para o site*/}
                <meta name="keywords" content=""/>{/*Palavras chave separadas por vírgulas*/}
                <meta name="author" content="FGV Jr." />{/*Autor do site*/}

                {/*SMO(social media otimization)*/}
                <meta property="og:title" content="" />
                <meta property="og:site_name" content="" />
                <meta property="og:description" content="" />
                <meta property="og:url" content="" />
                <meta property="og:image" content="" />
                <meta property="og:image:type" content="image/" />
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css"/>
                <link rel="preconnect" href="https://fonts.googleapis.com"/>
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>

            </Head>
            
            <Component {...pageProps} />
        </>
    )
}