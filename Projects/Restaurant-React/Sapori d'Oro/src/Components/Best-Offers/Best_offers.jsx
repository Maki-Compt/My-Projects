import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHeart} from '@fortawesome/free-solid-svg-icons'
import styles from "./Best_Offers.module.css"
import sushi from "../../assets/comidas/1977354_b381596e8b118ce.jpg"
import arroz from "../../assets/comidas/arroz-de-marisco-KitchenerPortugueseClub.jpg"
import bacalhau from "../../assets/comidas/bacalhau-a-bras.jpg"
import galinha from "../../assets/comidas/Best-Chicken-Tikka-Masala-IMAGE-2.jpg"
import tacos from "../../assets/comidas/BestTacosInMexicoCity.jpg"
import Cabrito from "../../assets/comidas/Cabrito Assado.jpg"
import caldo_verde from "../../assets/comidas/caldo-verde.jpg"


function Best_Offers() {
    return(<>
        <div className={styles.offers_container}>
            <h2>Melhores Ofertas</h2>

            <div className={styles.card_offers_container}>

                <div className={styles.offer_card}>
                    <img src={sushi} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Sushi</h2>
                    <p>Preço: 12€</p>
                </div>

                <div className={styles.offer_card}>
                    <img src={arroz} alt="arroz" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Arroz de Marisco</h2>
                    <p>Preço: 12€</p>
                </div>
                
                <div className={styles.offer_card}>
                    <img src={bacalhau} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Bacalhau à Brás</h2>
                    <p>Preço: 18€</p>
                </div>

                   <div className={styles.offer_card}>
                    <img src={galinha} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Galinha Tikka Masala</h2>
                    <p>Preço: 10€</p>
                </div>
                
                <div className={styles.offer_card}>
                    <img src={tacos} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Tacos</h2>
                    <p>Preço: 8€</p>
                </div>
                
                <div className={styles.offer_card}>
                    <img src={Cabrito} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Cabrito Assado</h2>
                    <p>Preço: 20€</p>
                </div>
                
                <div className={styles.offer_card}>
                    <img src={caldo_verde} alt="sushi" />
                    <div className={styles.top_card}><h3>Exóticos</h3><FontAwesomeIcon icon={faHeart} /></div>
                    <h2>Caldo Verde</h2>
                    <p>Preço: 7.5€</p>
                </div>
                
                

            </div>

        </div>
    </>)
}

export default Best_Offers