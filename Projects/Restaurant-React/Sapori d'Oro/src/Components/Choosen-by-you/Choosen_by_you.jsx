import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHeart} from '@fortawesome/free-solid-svg-icons'
import styles from "./Choosen_by_you.module.css"
import cozido from "../../assets/comidas/cozido-a-portuguesa-617.jpg"
import feijoada from "../../assets/comidas/Feijoada-a-brasileira.jpg"
import Sardine from "../../assets/comidas/Grilled_Sardines_5.50€_Marisqueira_O_Varino_Nazaré_(3785526688).jpg"
import croissant from "../../assets/comidas/historia-do-croissant-1920w.webp"
import Kebab from "../../assets/comidas/kebab3-e1744645266383.jpg"
import Leitão from "../../assets/comidas/Leitão-da-Bairrada.jpg"
import Hamburguer from "../../assets/comidas/origem-do-hambuguer-cnn4.webp"


function Choosen_by_you() {
    return(<>
        <div className={styles.offers_container}>
            <h2>Escolhidos para si</h2>

            <div className={styles.card_offers_container}>

                <div className={styles.offer_card}>
                    <img src={cozido} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Cozido à Portuguesa</h2>
                    <p>Preço: 15€</p>
                </div>

                <div className={styles.offer_card}>
                    <img src={feijoada} alt="arroz" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Feijoada Brasileira</h2>
                    <p>Preço: 12€</p>
                </div>
                
                <div className={styles.offer_card}>
                    <img src={Sardine} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Sardinha Grelhada</h2>
                    <p>Preço: 14€</p>
                </div>

                   <div className={styles.offer_card}>
                    <img src={Kebab} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Kebab</h2>
                    <p>Preço: 25€</p>
                </div>
                
                <div className={styles.offer_card}>
                    <img src={croissant} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Croissant Francês</h2>
                    <p>Preço: 8€</p>
                </div>
                
                <div className={styles.offer_card}>
                    <img src={Leitão} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Leitão da Bairrada</h2>
                    <p>Preço: 30€</p>
                </div>
                
                <div className={styles.offer_card}>
                    <img src={Hamburguer} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Hamburguer Americano</h2>
                    <p>Preço: 7.5€</p>
                </div>
                
            </div>

        </div>
    </>)
}

export default Choosen_by_you