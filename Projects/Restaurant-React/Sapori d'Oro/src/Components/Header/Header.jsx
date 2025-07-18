import styles from "./Header.module.css"
import Hero_logo_img from "../../assets/Logo-header.png"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBars} from '@fortawesome/free-solid-svg-icons'

function Header() {
    return(
        <>
            <header className={styles.header}>
                <nav>

                    <div className={styles.logo_block}>
                        <img src={Hero_logo_img} alt="Image of a cartoonish Pizza"/>
                        <h2>Sapori d'Oro</h2>
                    </div>

                    <ul>
                        <li>Home</li>
                        <li>Ajuda</li>
                        <li>Contactos</li>
                        <li>Politicas</li>
                        <li>FQAs</li>
                    </ul>
                    
                    <FontAwesomeIcon icon={faBars} className={styles.menu}/>

                </nav>
            </header>
        </>
    )
}

export default Header