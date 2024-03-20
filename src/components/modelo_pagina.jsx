import { Children } from "react";
import Sidebar from "./sidebar";

export default function Pagina(props) {

    const titulo = props.titulo

    return (
        <div className="pagina">
            <Sidebar/>
            <h1>{titulo}</h1>

            <div className="graficos">
                {props.children}
            </div>
        </div>
    )
}