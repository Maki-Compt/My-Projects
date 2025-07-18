import chef from "../../assets/flex-off.webp"
import styles from "./flex_off.module.css"

function flex_off() {
    return(<>
        <div className={styles.flex_off}>
            <div className="text_part"><h1>Descubra os Melhores Pratos do Mundo!</h1></div>
            <img src={chef} alt="smily woman chef"/>
        </div>
    </>)
}

export default flex_off