import styles from "./Dishes.module.css"
import asian from "../../assets/Dishes/Asiático.jpg"
import Brasileiro from "../../assets/Dishes/Brasileiro.jpg"
import chines from "../../assets/Dishes/Chinês.webp"
import frances from "../../assets/Dishes/Francês.webp"
import Indiano from "../../assets/Dishes/Indiano.jpg"
import Italiano from "../../assets/Dishes/Italiano.webp"
import Latino from "../../assets/Dishes/Latino.jpg"
import Japonês from "../../assets/Dishes/Japonês.jpg"
import Mexican from "../../assets/Dishes/Mexicano.jpg"
import Portugues from "../../assets/Dishes/Português.webp"
import arrow from "../../assets/Arrow_right.png"
import { useRef, useEffect } from "react"

function Dishes() {
       

    return(<>
        <div className={styles.main_one}>

            <h2>Tipos de Pratos</h2>

            <div className={`${styles.arrow} ${styles.left_arrow}`} ><img src={arrow} alt="" /></div>
            <div className={`${styles.arrow} ${styles.right_arrow}`} ><img src={arrow} alt="" /></div>
        

            <div className={styles.dish_container}>

      
                <div className={styles.dish}>
                    <img src={asian} alt="Prato Asiático"/>
                    <h3>Asiático</h3>
                </div>

                <div className={styles.dish}>
                    <img src={Brasileiro} alt="Prato Brasileiro"/>
                    <h3>Brasileiro</h3>
                </div>

                <div className={styles.dish}>
                    <img src={chines} alt="Prato Chinês"/>
                    <h3>Chinês</h3>
                </div>

                
                <div className={styles.dish}>
                    <img src={frances} alt="Prato Francês"/>
                    <h3>Francês</h3>
                </div>

                <div className={styles.dish}>
                    <img src={Indiano} alt="Prato Francês"/>
                    <h3>Indiano</h3>
                </div>

                <div className={styles.dish}>
                    <img src={Italiano} alt="Prato Francês"/>
                    <h3>Italiano</h3>
                </div>
                
                <div className={styles.dish}>
                    <img src={Japonês} alt="Prato Francês"/>
                    <h3>Japonês</h3>
                </div>

                <div className={styles.dish}>
                    <img src={Mexican} alt="Prato Francês"/>
                    <h3>Mexicano</h3>
                </div>

                <div className={styles.dish}>
                    <img src={Portugues} alt="Prato Francês"/>
                    <h3>Português</h3>
                </div>


            </div>

        </div>
    </>)
}

export default Dishes