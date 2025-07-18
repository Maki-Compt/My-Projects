import chef from "../../assets/side-view-female-chef-kitchen-slicing-vegetables-compressed-scaled.jpg"
import styles from "./subscribe.module.css"

function subscribe() {
    return(<>
        <div className={styles.subscribe}>
            <img src={chef} alt="female chef"/>
            <div className={styles.left_side}>
                <h2>Já é cliente subscrito?</h2>
                <p>Subscreva-se a nossa newsletter pra se actualizar mais sobre as novidades de pratos exóticos no momento meu nobre.</p>
                <button>Subscrever</button>
            </div>
        </div>
    </>)
}

export default subscribe