import styles from "./footer.module.css"

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFacebook} from "@fortawesome/free-brands-svg-icons";
import { faTwitter} from "@fortawesome/free-brands-svg-icons";
import { faInstagram} from "@fortawesome/free-brands-svg-icons";
import { faLinkedin} from "@fortawesome/free-brands-svg-icons";
import { faTwitch} from "@fortawesome/free-brands-svg-icons";
import { faYoutube} from "@fortawesome/free-brands-svg-icons";

import play_store from "../../assets/footer/2.webp"
import apple_store from "../../assets/footer/3.webp"

function footer() {
    return(<>
        <div className={styles.footer}>

            <div className={styles.footer_top}>

                <div className={styles.apps}>

                    <h3>Transfira a nossa aplicação</h3>
                    <div className={styles.app}>
                        <img src={play_store} alt="" />
                        <img src={apple_store} alt="" />
                    </div>

                </div>

                <div className={styles.list}>
                    <ul>
                        <li>Sobre nós</li>
                        <li>Informação de Contactos</li>
                        <li>Tem restaurante?</li>
                        <li>Perguntas frequentes</li>
                        <li>Estamos a contratar</li>
                        <li>Restaurantes pertos de mim</li>
                    </ul>
                </div>

                <div className={styles.list}>
                    <ul>
                        <li>Programa de fidelização</li>
                        <li>Termos de utilização</li>
                        <li>Declaração de Privacidade e Cookies</li>
                        <li>Permissão para instalção de Cookies</li>
                        <li>Parceria Guia MICHELIN</li>
                        <li>Restaurantes pertos de mim</li>
                    </ul>
                </div>

                <div className={styles.we_are}>
                    <h3>Pode encontrar-nos em</h3>
                    <div className={styles.icons}>
                        <FontAwesomeIcon icon={faFacebook} className={styles.icon}/>
                        <FontAwesomeIcon icon={faTwitter} className={styles.icon}/>
                        <FontAwesomeIcon icon={faInstagram} className={styles.icon}/>
                        <FontAwesomeIcon icon={faLinkedin}className={styles.icon} />
                        <FontAwesomeIcon icon={faTwitch} className={styles.icon}/>
                        <FontAwesomeIcon icon={faYoutube}className={styles.icon}/>
                    </div>
                </div>

            </div>

            <div className={styles.footer_bottom}>
                <p className={styles.footer_bottom_top}>
                    As ofertas promocionais estão sujeitas às condições apresentadas na página do restaurante. As ofertas relativas a bebidas alcoólicas reservam-se, estritamente, a adultos. O consumo abusivo de álcool é perigoso para a saúde. Beba com moderação.
                </p>
                <p className={styles.footer_bottom_bottom}>
                    &copy;2025 Sapori d'Oro todos os direitos reservados.
                </p>
            </div>
        </div>
    </>)    
}

export default footer